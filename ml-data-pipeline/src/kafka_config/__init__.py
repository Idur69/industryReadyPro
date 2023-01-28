
import os



# Cloud API details
API_KEY = "N3LZNTGVW7LC7NSA" #os.getenv('API_KEY',None)
API_SECRET_KEY = "lH0PEjfzWZwXqSgNuq2hlOGCD7giaOS0T0q5ZZXDCRIVDz2ZA+RVcCFhZNOJHtTb" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

# Authentication related variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"


#Schema related variable
SCHEMA_REGISTRY_API_KEY = "GI4NZNJAZU2FFQNN" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "tsPpCj5/Uj7QN/rwF1KmdQHCMFXuZpjMipcPO0YwJ7lzjglR1pF0VfOjdt7cYBds" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-10wgj.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

