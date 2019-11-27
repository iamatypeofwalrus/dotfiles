#!/usr/bin/env ruby
require 'json'

SPACE_FN = "SpaceFn"
SPACE_FN_VARIABLE = "spacefn_mode"
KARABINER_CONFIG = File.join(__dir__, "..", "dotfiles", "config", "karabiner", "karabiner.json")

def generate_space_fn_mapping(from, to, modifier=nil)
  first = {
    type: "basic",
    parameters: {
      "basic.simultaneous_threshold_milliseconds" => 450
    },
    from: {
      simultaneous: [
        {
          key_code: "spacebar"
        },
        {
          key_code: from
        }
      ],
      "simultaneous_options" => {
        "key_down_order" => "strict",
        "key_up_order" => "strict_inverse",
        "key_up_when" => "all",
        "to_after_key_up" => [
          {
            "set_variable" => {
              name: SPACE_FN_VARIABLE,
              value: 0
            }
          }
        ]
      },
      modifiers: {
        optional: [
          :any
        ]
      }
    },
    to: [
      {
        key_code: to
      },
      {
        set_variable: {
          name: SPACE_FN_VARIABLE,
          value: 1
        }
      }
    ]
  }

  second = {
    type: "basic",
    conditions: [
      {
        name: SPACE_FN_VARIABLE,
        type: "variable_if",
        value: 1
      }
    ],
    from: {
      key_code: from,
      modifiers: {
        optional: [
          :any
        ]
      }
    },
    to: [
      {
        key_code: to
      }
    ]
  }

  if modifier
    first[:to].first[:modifiers] = [modifier]
    second[:to].first[:modifiers] = [modifier]
  end

  [first, second]
end

def generate_space_fn_rule
  {
    description: SPACE_FN,
    manipulators: [
      generate_space_fn_mapping("j", "down_arrow"),
      generate_space_fn_mapping("k", "up_arrow"),
      generate_space_fn_mapping("l", "right_arrow"),
      generate_space_fn_mapping("h", "left_arrow"),
      generate_space_fn_mapping("u", "home"),
      generate_space_fn_mapping("i", "end"),
      generate_space_fn_mapping("d", "9", "right_shift"), #
      generate_space_fn_mapping("f", "0", "right_shift"), # )
      generate_space_fn_mapping("e", "open_bracket", "right_shift"), # {
      generate_space_fn_mapping("r", "close_bracket", "right_shift"), # }
      generate_space_fn_mapping("c", "open_bracket"), # [
      generate_space_fn_mapping("v", "close_bracket"), # ]
      generate_space_fn_mapping("g", "equal_sign"), # =
      generate_space_fn_mapping("t", "equal_sign", "right_shift"), # +
      generate_space_fn_mapping("s", "hyphen"), # -
      generate_space_fn_mapping("a", "hyphen", "right_shift"), # _
      generate_space_fn_mapping("q", "backslash", "right_shift"), # |
      generate_space_fn_mapping("w", "backslash") # \
    ].flatten
  }
end


def main
  config = File.open(KARABINER_CONFIG) do |f|
    JSON.parse(f.read)
  end

  profile = config["profiles"].shift

  profile["complex_modifications"]["rules"].delete_if {|x| x["description"] == SPACE_FN}
  profile["complex_modifications"]["rules"] << generate_space_fn_rule
  config["profiles"].unshift(profile)

  puts JSON.pretty_generate(config)
end

main
