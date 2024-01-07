import pymongo
import streamlit as st
import yaml
import streamlit_authenticator as stauth

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
def create_user(db, userID, pwd):
    if not userID or not pwd:
        st.error("User ID or password cannot be empty.")
        return False
    
    # Assuming stauth.Hasher is correctly imported and defined
    userID_hash = hash(userID)
    pwd_hash = hash(pwd)

    st.write(userID_hash)
    
    try:
        # Check if USERID already exists
        users_collection = db["users"]
        existing_user = users_collection.find_one({"userID_hash": userID_hash})
        st.write(existing_user)

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
                        "problem_submitted": 'ipsum',
                        "solution_submitted": 'ipsum',
                        "score": 100,
                        "lean_problem": 'ipsum',
                        "lean_solution": 'ipsum',
                        "key_metrics": 'ipsum',
                        "uniq_val_prop": 'ipsum',
                        "unfair_advng": 'ipsum',
                        "channels": 'ipsum',
                        "customer_seg": 'ipsum',
                        "cost_struct": 'ipsum',
                        "rev_streams": 'ipsum'
                    }
                ]
            }

            # Insert the new user into the database
            result = users_collection.insert_one(new_user)

            # Check if insertion was successful
            if result.inserted_id:
                st.success("User created successfully.")
                return True
            else:
                st.error("Error creating user.")
                return False

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False




