#!/usr/bin/env python
import sys
import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime 
import logging

# setup logging
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('elastic-statistics')

# set content-type
elastic_headers = {'Content-type': 'application/json'}

# get elastic cluster statistics
elastic_stats = requests.get('http://localhost:9200/_nodes/stats').json()

if (elastic_stats):
    elastic_nodes_data = elastic_stats['nodes']
    if (elastic_nodes_data):
        elastic_bulk_data = ''
        for node_id in elastic_nodes_data:
            node_data = elastic_nodes_data[node_id]
            # name of node
            node_name = node_data['name']
            if (node_name and node_data):
                #elastic_bulk_data += '{"_index": "nodes_stats", "_type": "' + node_name + '"}\n'
                elastic_bulk_data += '{"index": {"_index": "nodes_stats", "_type": "' + node_name + '"}}\n'
                elastic_bulk_data += json.dumps(node_data) + '\n'
                if (elastic_bulk_data != ''):
                    logger.info("%s" % elastic_bulk_data)
                    response = requests.post('http://localhost:9200/_bulk', 
                               headers= elastic_headers, data=elastic_bulk_data)
                    if response.status_code == 200:
                        logger.info("Elastic nodes statistics updated sucessfully.\n") 
                        logger.info(response.text)

