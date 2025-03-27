
### Elastic

#### KQL (Kibana Query Language)

finding php files in web server logs
`message: *.php and not message: *index.php*`

if we want to remove 404s too
`and not response: 404`


