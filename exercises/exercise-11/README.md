# Exercise:

Write a script that takes a directory and converts each .yaml file into a corresponding .json file.

# Example:

YAML:
```yaml
apis:
    - name: login
      port: 8080
    - name: profile
      port: 8090
```
JSON:
```json
{
    "apis": [
        {
            "name": "login",
            "port": 8080
        },
        {
            "name": "profile",
            "port": 8090
        }
    ]
}
```