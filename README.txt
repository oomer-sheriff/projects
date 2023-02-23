thanks for using this ai powered music recommendation chatbox
you need to install a few libraries before running this module
pip install openai
pip install requests
pip install json
pip install flask
you would also require a new spotify api token as it expires everyone one hour
instructions on using input and output of this module:
1. the user starts the conversation
2. the ai replies and you get a prompt to continue or stop and if you stop you get a spotify link playlist according to the 
    mood of your conversation with the ai
3. if the ai doesnt reqply properly or simply uses a "?" or "." ,use a "?" as the next input

for getting a spotify api token;
https://developer.spotify.com/console/get-playlist/ 
go here and scroll all the way down till you find "get token" button
check all boxes and get the token from there and use it in line 44 of the code 
headers-> authorization-> "Bearer {new token}" 
or just contact to phone : 9361910960

  NOTE: frontend of the project is under development so kindly use the module for verification
