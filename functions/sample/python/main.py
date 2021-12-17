#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):
    databaseName = "dealerships"
    print("Hello")

    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))
        dbs_output = client["reviews"]
        type_of_dbs_output = type(dbs_output)
        print(f"type-of-dealerships: {type_of_dbs_output}, dealerships: {dbs_output}")
        
        print("Count:", dbs_output.doc_count())
        keys_in_dict = dbs_output.keys(remote=True)
        for key_i in keys_in_dict:
            value_i = dbs_output.get(key_i, remote=True)
            print(f"({key_i} : {value_i})")
        print(dbs_output)

    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}


###########################
if __name__ == '__main__':
    login_dict = {
        "COUCH_URL": "https://9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "YE7undQzSOjWO9FYgY3AIpv7GxGvr9yhL1prUay-HWPv",
        "COUCH_USERNAME": "9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix"
    }
    main(login_dict)
