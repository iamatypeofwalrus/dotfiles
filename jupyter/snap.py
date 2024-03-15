# @title Code: PCS Product Filter Parsing
# filter.py is a set of functions that operate on product set filters. It is intended to be used with Pandas to help generate
#           insights into how customers use product set filters e.g. which columns are used most in filters? which operators are used the most?
#
# iter_filter is a generator method that given a product set filter as a Python dict (could be created from json.loads())
# it will yield the column, operator_name, and the value supplied to the operator.
#
# get_columns_in_filter returns a list of all the columns used in a filter, including duplicates. this can be handy
# if you want a true count of the times a column is referenced in a filter
#
# get_uniq_columns_in_filter returns a list of all of the uniq PCS columns used in a filter
PCS_FILTER_LOGICAL_OPERATORS = {
    'and',
    'or'
}

# iter_filter yields column, operator name, value supplied to operator
def iter_filter(filter: dict):
    # yield the column, operator, and value
    for key, value in filter.items():
        # [{'custom_label_0': {'i_contains': '#gl_home#'}}, {'availability': {'eq': 'IN_STOCK'}}]
        # {'OR': [{'TITLE': {'I_CONTAINS': 'بكج'}}, {'AND': [{'TITLE': {'I_CONTAINS': 'باقة'}}]}]}
        key = key.lower()

        if key in PCS_FILTER_LOGICAL_OPERATORS:
            # recurse!
            # assuming this is an array filters. valid?
            for val in value:
                yield from iter_filter(val)
        else:
            # base case
            col = key
            operators_and_values = [x for x in value.items()]

            for operator, value in operators_and_values:
                yield col, operator, value

def get_columns_in_filter(filter: dict) -> list:
    cols = []
    for col, _, _, in iter_filter(filter):
        cols.append(col)

    return cols

def get_uniq_columns_in_filter(filter: dict) -> list:
    cols = get_columns_in_filter(filter)
    return list(set(cols))

# @title Code: Google Product Category
import os
import requests

# This file contains two classes: GoogleProductCategoryTaxonomy and GoogleProductCategory
#
#   GoogleProductCategoryTaxonomy: models the taxonomy and provides entrance methods into the taxonomy eg get_by_name and get_by_gpc_id
#
#   GoogleProductCategory: models an individual Google Product Category Node eg <Educational Flash Cards>. From this node you can walk back
#                          up the taxonomy e.g #lineage. The class also contains methods to compare GPCs to each eg longest continues branch between two
#                          categories eg #number_of_shared_branches
#
# To build a Taxonomy call GoogleProductCategoryTaxonomy.build_taxonomy() or GoogleProductCategoryTaxonomy.build_taxonomy("https://www.google.com/basepages/producttype/taxonomy-with-ids.en-GB.txt") if you
# wish to build a taxonomy for a different localization.
#
# All taxonomy files are cached under /tmp so subsequent calls to GoogleProductCategoryTaxonomy.build_taxonomy() will be local
#
# gpc_taxonomy_en_us = GoogleProductCategoryTaxonomy.build_taxonomy()
class GoogleProductCategoryTaxonomy:

    cache_dir = "/tmp"
    taxonomy_url_en_US = "https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt"
    taxonomy_url_en_GB = "https://www.google.com/basepages/producttype/taxonomy-with-ids.en-GB.txt"

    def __init__(self, localization: str) -> None:
        self.localization = localization
        self.root = None
        self.gpc_by_id = {}
        self.gpc_by_name = {}

    def __str__(self):
        return  f"GoogleProductCategoryTaxonomy(localization={self.localization})"

    @classmethod
    def build_taxonomy(self, url=taxonomy_url_en_US):
        return self.build_taxonomy_from_url(url)

    @classmethod
    def build_taxonomy_from_url(self, url, bust_taxonomy_file_cache=False):
        # "https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt"
        filename = url.split("/")[-1]
        file = self.__cache_key(filename)
        self.__cache_taxonomy_file(file, url, bust_cache=bust_taxonomy_file_cache)

        # taxonomy-with-ids.en-US.txt
        localization = filename.split('.')[1]

        root = GoogleProductCategory.new_root()
        taxonomy = GoogleProductCategoryTaxonomy(localization=localization)
        taxonomy.root = root

        self.__build_taxonomy_from_file(file, root, taxonomy)

        return taxonomy

    def get_by_name(self, category_name):
        normalized_name = GoogleProductCategory.normalize_category_name(category_name)
        return self.gpc_by_name.get(normalized_name, None)

    def get_by_id(self, gpc_id):
        return self.gpc_by_id.get(gpc_id, None)

    def is_google_product_category(self, category_name):
        # opting to return false here instead of raising as this method
        # can be used on raw catalog data and we'd rather not throw. False
        # tells us just as much
        if not isinstance(category_name, str):
            return False

        return GoogleProductCategory.normalize_category_name(category_name) in self.gpc_by_name

    def is_google_product_category_id(self, gpc_id) -> bool:
        if not isinstance(gpc_id, (int, float)):
            return False

        return gpc_id in self.gpc_by_id

    @classmethod
    def __build_taxonomy_from_file(self, file, root, taxonomy):
        for gpc_id, gpc in self.__gpc_taxonomy_generator(file):
            gpc = GoogleProductCategory.normalize_category_name(gpc)
            gpc_id = int(gpc_id)

            categories = gpc.split(" > ")
            curr_node = root

            # this algorithm works because the taxonomy file is ordered by depth
            # otherwise in the `else` block we wouldn't know the gpc_id of the new node
            for category in categories:
                # check if there is a child in the current node with this name
                potential_matches = [x for x in curr_node.children if x.category_name == category]
                # There should be at most 1 match
                if len(potential_matches) > 1:
                    raise Exception("Multiple matches found for category: " + category)
                elif len(potential_matches) == 1:
                    curr_node = potential_matches[0]
                else:
                    new_node = GoogleProductCategory(category, gpc_id)

                    taxonomy.gpc_by_id[gpc_id] = new_node
                    taxonomy.gpc_by_name[gpc] = new_node

                    new_node.set_parent(curr_node)
                    curr_node.add_child(new_node)
                    curr_node = new_node

    @classmethod
    def __cache_key(self, filename):
        return f"{self.cache_dir}/{filename}"

    @classmethod
    def __cache_taxonomy_file(self, file, url, bust_cache=False):
        if bust_cache or not os.path.exists(file):
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()

                with open(file, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while downloading the file to {file}:", e)
                raise e

    @classmethod
    def __gpc_taxonomy_generator(self, taxonomy_file):
        with open(taxonomy_file) as file:
            seen = 0

            for line in file:
                seen += 1
                if seen == 1:
                    continue

                line = line.strip()
                row = line.split(" - ", 1)

                if len(row) != 2:
                    raise Exception("Invalid row: " + line)

                gpc_id = row[0]
                gpc = row[1]

                yield gpc_id, gpc



class GoogleProductCategory:

    def __init__(self, category_name, gpc_id):
        self.category_name = category_name
        self.gpc_id = gpc_id
        self.parent = None
        self.children = set()

    ############# Read methods

    # lineage returns all the nodes in a GPC's branch from the Root Category node eg Apparel & Accessories down to the node itself.
    def lineage(self):
        lineage = [x for x in self.iterate_over_gpc_branch(self)]
        lineage.reverse()

        return lineage

    # print_branch prints the entire lineage as a string eg animals & pet supplies > pet supplies > bird supplies > bird cage accessories > bird cage bird baths
    def print_branch(self):
        lineage_names = [x.category_name for x in self.lineage()]

        return " > ".join(lineage_names)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def has_ancestor_with_id(self, ancestor_gpc_id):
        curr_node = self
        while not curr_node.is_root():
            if curr_node.gpc_id == ancestor_gpc_id:
                return True
            else:
                curr_node = curr_node.parent

        return False

    def get_root_category(self):
        curr_node = self
        while not curr_node.is_root():
            if curr_node.parent.is_root():
                return curr_node
            else:
                curr_node = curr_node.parent

        return None

    # get_ancestor_at_level allows you to take a GPC eg Animals & Pet Supplies > Pet Supplies > Bird Supplies
    # and get the ancest at specific level eg 1 would return Animals & Pet Supplies, 2 returns Animals & Pet Supplies > Pet Supplies
    def get_ancestor_at_level(self, level):
        if level < 1:
            raise "must be at least 1"

        lineage = self.lineage()

        # if we want level 3 and our lineage is only 3 deep return as far down as we could go
        if len(lineage) < level:
            return lineage[-1]
        else:
            return lineage[level - 1]

    # 0 -> the two GPC's do not share any branch
    # 1, N -> the two GPC's share a single branch, but the last branch is different
    def number_of_shared_branches(self, other_gpc):
        gpc_lineage = self.lineage()
        other_gpc_lineage =  other_gpc.lineage()

        # find the first index where the two lists diverge
        for i in range(min(len(gpc_lineage), len(other_gpc_lineage))):
            if gpc_lineage[i] != other_gpc_lineage[i]:
                return i

        # if we get here, the two lists are the same up to the length of the shortest lineage
        return min(len(gpc_lineage), len(other_gpc_lineage))

    # iterate_over_gpc_branch walks from the GPC node back up the taxonomy and yields every node, including itself,
    # along the way.
    #
    # this method will never return the root node
    def iterate_over_gpc_branch(self, gpc):
        curr_node = gpc
        while not curr_node.is_root():
            yield curr_node
            curr_node = curr_node.parent

    ############# Write Methods

    def add_child(self, child):
        if child in self.children:
            raise ValueError("child already in set")
        else:
            self.children.add(child)

    def set_parent(self, parent):
        self.parent = parent

    def set_gpc_id(self, gpc_id):
        self.gpc_id = gpc_id

    def parent(self):
        return self.parent

    ############# Class Methods

    @classmethod
    def normalize_category_name(self, category_name):
        return category_name.strip().lower()

    @classmethod
    def new_root(self):
        return GoogleProductCategory('root', 0)

    ########### Representation methods

    def __str__(self):
        return  f"Category({self.category_name}, gpc_id={self.gpc_id})"

    # allows for recursive printing
    def __repr__(self):
        return self.__str__()

    # in case we want to put in a dict or set
    def __hash__(self) -> int:
        return hash(self.category_name)

    # needed for "not in" array check
    def __eq__(self, other) -> bool:
        if isinstance(other, GoogleProductCategory):
            return self.gpc_id == other.gpc_id

        return False

# Big Query
def table_v1_products(year_month_day_str):
  return f"snapchat-pcs-prod.v1.products_{year_month_day_str}"

def table_v1_catalogs(year_month_day_str):
  return f"snapchat-pcs-prod.v1.catalogs_{year_month_day_str}"

def table_product_repo(year_month_day_str):
  return f"snapchat-pcs-prod.product_data_for_ranking.products_annotated_{year_month_day_str}"