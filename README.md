# WebApollo API Library

Apollo is a Python library for interacting with [WebApollo](https://github.com/gmod/apollo/)

## Examples

```python
from apollo import WebApolloInstance
wa = WebApolloInstance('https://fqdn/apollo', 'jane.doe@fqdn.edu', 'password')

orgs = wa.organisms.addOrganism(
    "Yeast",
    "/path/to/jbrowse/data",
    genus='Saccharomyces',
    species='cerevisiae',
    public=False
)

# Give webapollo a second to process the uploaded organism.
time.sleep(1)

# Then add yourself to permission list
data = wa.users.updateOrganismPermission(
    wa.me, "Yeast",
    write=True,
    export=True,
    read=True,
)
```

## TODO

- [ ] Testing (use erasche/webapollo2:latest)
- [ ] Document methods
    - [ ] Ensure methods behave properly

## License

Available under the MIT License
