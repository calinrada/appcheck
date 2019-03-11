# These values can be retrieved from an env or from a data store
INJECTION_TYPES = {
    "DATABASE_USERNAME": "%' or 0=0 union select null, user() #",
    "DATABASE_VERSION": "%' or 0=0 union select null, version() #"
}
