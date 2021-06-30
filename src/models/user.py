class User(object):
    def __init__(
            self, id: int, name: str, username: str, email: str, address: str, phone: str, website: str, company: str):
        self.id = id
        self.name = name
        self.user_name = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def __str__(self):
        text = "id: %s, name: %s, username: %s, email: %s, address: %s, phone: %s, website: %s, company: %s" % (self.id,
                                                                                                                self.name,
                                                                                                                self.user_name,
                                                                                                                self.email,
                                                                                                                self.address,
                                                                                                                self.phone,
                                                                                                                self.website,
                                                                                                                self.company)
        return text


__USER_SCHEMA = {

    "id": {"type": "integer", "required": True},
    "name": {"type": "string"},
    "username": {"type": "string"},
    "email": {
        "type": "string",
        "required": True,
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    },
    "address": {
        "type": "dict",
        "schema": {
            "street": {"type": "string"},
            "suite": {"type": "string"},
            "city": {"type": "string"},
            "zipcode": {"type": "string"},
            "geo": {
                "type": "dict",
                "schema": {
                    "lat": {"type": "string"},
                    "lng": {"type": "string"}
                }
            }
        }
    },
    "phone": {"type": "string"},
    "website": {"type": "string"},
    "company": {
        "type": "dict",
        "schema": {
            "name": {"type": "string"},
            "catchPhrase": {"type": "string"},
            "bs": {"type": "string"}
        }
    }
}


def get_user_schema():
    return __USER_SCHEMA
