import pymongo
import streamlit as st
import yaml
import streamlit_authenticator as stauth
import hashlib as hl
def db_init():
    client = pymongo.MongoClient("mongodb+srv://jiashuchen:" 
                                + st.secrets["mongo_password"] 
                                + "@cluster0.epj60wr.mongodb.net/?retryWrites=true&w=majority")

    return client.myDatabase

# Schema design
# Each object in the collection "users" should have the following stucture:
'''
{ userID_hash: 'iidjjhasdfl2kjwhds',
  pwd_hash: 'asdf2lohkjhl89ihfdsa',
  data: [
    { problem_submitted: 'ipsum',
      solution_submitted: 'ipsum',
      score: 100,
      lean_problem: 'ipsum',
      lean_solution: 'ipsum',
      key_metrics: 'ipsum',
      uniq_val_prop: 'ipsum',
      unfair_advng: 'ipsum',
      channels: 'ipsum',
      customer_seg: 'ipsum',
      cost_struct: 'ipsum',
      rev_streams: 'ipsum'}
      
  ]
}
'''
# The userID_hash is assumed to be the UUID. Must enforce unique userID_hash upon user registration.
# Will allow duplicate passwords, and skip salting the passwords for simplicity.


# Create an user based on USERID and PASSWORD, both of which would be passed in as plain-texts.
# Check if USERID exists in USERS database. Reject creation request if fulfilling such intent would result in
# duplicate USERID in the database. Returns TRUE if successful, FALSE otherwise.
def create_user(db, userID_hash, pwd_hash):
    try:
        # Check if USERID already exists
        users_collection = db["users"]
        existing_user = users_collection.find_one({"userID_hash": userID_hash})

        if existing_user:
            st.error("User already exists. Creation request rejected.")
            return False
        else:
            # Create a new user
            new_user = {
                "userID_hash": userID_hash,
                "pwd_hash": pwd_hash,
                "data": [
                    {
                        "problem_submitted": '',
                        "solution_submitted": '',
                        "score": -1,
                        "lean_problem": '',
                        "lean_solution": '',
                        "key_metrics": '',
                        "uniq_val_prop": '',
                        "unfair_advng": '',
                        "channels": '',
                        "customer_seg": '',
                        "cost_struct": '',
                        "rev_streams": ''
                    }
                ]
            }

            # Insert the new user into the database
            result = users_collection.insert_one(new_user)

            # Check if insertion was successful
            if result.inserted_id:
                return True
            else:
                return False

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

def authenticate_user(db, userID_hash, pwd_hash):
    users_collection = db["users"]
    cur_user = users_collection.find_one({"userID_hash": userID_hash})
    
    if (cur_user is None) or (cur_user.get("pwd_hash") != pwd_hash):
        return False
    
    return True



