# Elasticsearch cluster monitor using Grafana/Kibana

Using stats API, it is simple to get very useful elastic node(s) statistic . Please refer to https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html for more details.

This python script uses stats API to periodically poll the elastic cluster and get important cluster parameters for determining cluster health.

## Installation

### create the index
```
$ sh elastic-statistics-template.sh
```

### run the script
```
$ python elastic-statistics.py 
```
on one of the elastic cluster nodes.

Run it through unix crontab to start executing it periodically and generate elastic cluster statistics.

## Notes: 
* You need to create index first before running the elastic cluster statistics script.
* The statistics for an elastic node are indexed under a single type, identified by the node’s name. It is recommended to use fixed node names, otherwise any restart of elasticsearch will generate new node names and statistics for the node will be indexed under different types. So, be careful!!

## To-do
* Instead of cron, run the script using built-in python scheduler and control its run through supervisor daemon.
* Use curator to delete the old statistics
* Visualize elastic cluster statistics using Grafana/Kibana.

## Thank you
* The following Elastic discussion thread was useful to show bulk indexing using python:
https://discuss.elastic.co/t/need-help-to-create-a-python-script-to-create-index-on-cluster-helath-api/28834/2


