# cloudflare-location-updater
Script to update source IP address against a Cloudflare Zero Trust location.  Useful if you have a changing IP address.

It can be packaged as a container using the Dockerfile present in the repository.

The script expects the the following environment variables to be set

|Variable|Use|
|---|---|
|CF_ACCOUNT|ID of your Cloudflare account|
|CF_LOCATION|ID of the Cloudflare Zero Trust location you are updating|
|CF_LOCATION_NAME|Name of the Cloudflare Zero Trust location|
|CF_TOKEN|A cloudflare API token with appropriate scope to update a Cloudflare Zero Trust location|

The `manifests` directory contains example K8s manifests to run this as a cronjob every 5 mins.
