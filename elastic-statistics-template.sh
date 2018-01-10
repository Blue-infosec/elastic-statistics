#!/bin/bash

# Use the following command to create elastic mapping before running 'elastic-statistics.py' script.
# modify localhost to your elastic cluster address.

$ curl -H 'Content-Type: application/json' -XPUT 'http://localhost:9200/nodes_stats' -d '
{
    "settings" : {
        "number_of_shards" : 1,
        "number_of_replicas" : 1
    },

    "mappings" : {
        "_default_" : {
            "dynamic_templates" : [
            {
                "timestamps_as_date" : {
                    "match_pattern" : "regex",
                    "path_match" : ".*timestamp",
                    "mapping" : {
                        "type" : "date"
                    }
                }
            },
            {
                "strings_not_analyzed" : {
                    "match" : "*",
                    "match_mapping_type" : "string",
                    "mapping" : {
                        "type" : "keyword"
                    }
                }
            }
            ]
        }
    }
}'








