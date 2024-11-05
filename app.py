import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import joblib

# List of available genres for track_genre
track_genres = [
    'acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient',
    'anime', 'black-metal', 'bluegrass', 'blues', 'brazil',
    'breakbeat', 'british', 'cantopop', 'chicago-house', 'children',
    'chill', 'classical', 'club', 'comedy', 'country', 'dance',
    'dancehall', 'death-metal', 'deep-house', 'detroit-techno',
    'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm',
    'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk',
    'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove',
    'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle',
    'heavy-metal', 'hip-hop', 'honky-tonk', 'house', 'idm', 'indian',
    'indie-pop', 'indie', 'industrial', 'iranian', 'j-dance', 'j-idol',
    'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino',
    'malay', 'mandopop', 'metal', 'metalcore', 'minimal-techno', 'mpb',
    'new-age', 'opera', 'pagode', 'party', 'piano', 'pop-film', 'pop',
    'power-pop', 'progressive-house', 'psych-rock', 'punk-rock',
    'punk', 'r-n-b', 'reggae', 'reggaeton', 'rock-n-roll', 'rock',
    'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo',
    'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter',
    'soul', 'spanish', 'study', 'swedish', 'synth-pop', 'tango',
    'techno', 'trance', 'trip-hop', 'turkish', 'world-music'
]

encoder = joblib.load(r"D:\GUVI\Shahanaz_Final_Project\onehot_encoder.joblib")
model = joblib.load(r"D:\GUVI\Shahanaz_Final_Project\xgboost_model.joblib")
dummies_var = ["explicit","track_genre"]

# # Title of the app
# st.title("Spotify popularity classification")

# st.subheader("Enter Your Input Data")

# # Title of the app
# st.title("Feature Input App")

# # Arranging input fields in a 2x2 layout
# col1, col2 = st.columns(2)
# with col1:
#     duration_ms = st.number_input("Duration (ms)", min_value=8586.0, max_value=5237295.0, value=8586.0)
#     danceability = st.number_input("Danceability", min_value=0.0, max_value=1.0, value=0.0)
#     key = st.number_input("Key", min_value=0, max_value=15, value=0, step=1)
#     mode = st.selectbox("Mode", options=[0, 1], index=0)  # Set default to 0
#     instrumentalness = st.number_input("Instrumentalness", min_value=0.0, max_value=1.0, value=0.0)
#     valence = st.number_input("Valence", min_value=0.0, max_value=1.0, value=0.0)
#     acousticness = st.number_input("Acousticness", min_value=0.0, max_value=1.0, value=0.0)

# with col2:
#     explicit = st.selectbox("Explicit", options=["False", "True"])  # Set default to False
#     energy = st.number_input("Energy", min_value=0.0, max_value=1.0, value=0.0)
#     loudness = st.number_input("Loudness", min_value=-50.0, max_value=5.0, value=-50.0)
#     speechiness = st.number_input("Speechiness", min_value=0.0, max_value=1.0, value=0.0)
#     liveness = st.number_input("Liveness", min_value=0.0, max_value=1.0, value=0.0)
#     tempo = st.number_input("Tempo", min_value=0.0, max_value=250.0, value=0.0)

# # Track Genre selection below the 2x2 grid
# track_genre = st.selectbox("Track Genre", options=track_genres)

# # Button to submit and navigate to the output page
# if st.button("Submit"):
#     # Creating a dictionary with the inputs
#     data = {
#         "duration_ms": duration_ms,
#         "explicit": explicit,
#         "danceability": danceability,
#         "energy": energy,
#         "key": key,
#         "loudness": loudness,
#         "mode": mode,
#         "speechiness": speechiness,
#         "acousticness": acousticness,
#         "instrumentalness": instrumentalness,
#         "liveness": liveness,
#         "valence": valence,
#         "tempo": tempo,
#         "track_genre": track_genre
#     }

#     # Convert dictionary to DataFrame
#     data_df = pd.DataFrame([data])

#     # Go to the next page and display the output
#     st.session_state["data_df"] = data_df  # Store the data in session state for the next page
#     st.experimental_rerun()  # Rerun the app to navigate to the next page

# # Displaying output if available in session state
# if "data_df" in st.session_state:
#     st.title("Output Page")
#     st.subheader("Input Data in DataFrame Format")
#     st.write(st.session_state["data_df"])



# Initialize session state for form submission tracking
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Title of the app
st.title("Spotify Classification")

# Check if the form has been submitted
if not st.session_state["submitted"]:
    # Arranging input fields in a 2x2 layout
    col1, col2 = st.columns(2)
    with col1:
        duration_ms = st.number_input("Duration (ms)", min_value=8586.0, max_value=5237295.0, value=8586.0)
        danceability = st.number_input("Danceability", min_value=0.0, max_value=1.0, value=0.0)
        key = st.number_input("Key", min_value=0, max_value=15, value=0, step=1)
        mode = st.selectbox("Mode", options=[0, 1], index=0)  # Set default to 0
        instrumentalness = st.number_input("Instrumentalness", min_value=0.0, max_value=1.0, value=0.0)
        valence = st.number_input("Valence", min_value=0.0, max_value=1.0, value=0.0)
        acousticness = st.number_input("Acousticness", min_value=0.0, max_value=1.0, value=0.0)
    with col2:
        explicit = st.selectbox("Explicit", options=[False, True])  # Set default to False
        energy = st.number_input("Energy", min_value=0.0, max_value=1.0, value=0.0)
        loudness = st.number_input("Loudness", min_value=-50.0, max_value=5.0, value=-50.0)
        speechiness = st.number_input("Speechiness", min_value=0.0, max_value=1.0, value=0.0)
        liveness = st.number_input("Liveness", min_value=0.0, max_value=1.0, value=0.0)
        tempo = st.number_input("Tempo", min_value=0.0, max_value=250.0, value=0.0)
        time_signature = st.number_input("signature", min_value=0.0, max_value=5.0, value=0.0)
    track_genre = st.selectbox("Track Genre", options=track_genres)

    # Button to submit the form
    if st.button("Submit"):
        # Creating a dictionary with the inputs
        data = {
            "duration_ms": duration_ms,
            "explicit": explicit,
            "danceability": danceability,
            "energy": energy,
            "key": key,
            "loudness": loudness,
            "mode": mode,
            "speechiness": speechiness,
            "acousticness": 0.0,  # assuming you have a fixed value or additional input for this
            "instrumentalness": instrumentalness,
            "liveness": liveness,
            "valence": valence,
            "tempo": tempo,
            "time_signature": time_signature,
            "track_genre": track_genre
        }
        data2_test= pd.DataFrame([data])

        # Transform the selected columns of test data
        transformed_test_data = encoder.transform(data2_test[dummies_var])

        # Create a DataFrame for transformed test data
        transformed_test_df = pd.DataFrame(transformed_test_data, columns=encoder.get_feature_names_out(dummies_var))

        # Concatenate the transformed test columns with the rest of the test DataFrame
        test_data_encoded = pd.concat([data2_test.drop(columns=dummies_var).reset_index(drop=True), transformed_test_df], axis=1)
        # Save the data to session state and mark form as submitted

        print(test_data_encoded)

        # Model predict 
        pred = model.predict(test_data_encoded)
        st.session_state["predict"] = pred      #st.write(pred)
        st.session_state["submitted"] = True
        st.rerun()  # Refresh to display the output page

else:
    # Displaying the output page
    st.title("Output Page")
    # st.subheader("Input Data in DataFrame Format")
    
    # Convert prediction to human-readable text
    if st.session_state["predict"][0] == 1:
        st.write("The prediction result: **Popularity**")
    else:
        st.write("The prediction result: **No Popularity**")

    # Button to reset the form
    if st.button("Go Back"):
        st.session_state["submitted"] = False  # Reset form state
        st.rerun()  # Refresh to display the input page