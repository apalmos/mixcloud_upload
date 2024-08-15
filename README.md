# upload_media

this pipeline will convert mp4 to mp3 and upload both to YouTube and Mixcloud (respectively)

# convert mp4 to mp3

to convert mp4 to mp3 you just need to use the convert_mp4_to_mp3 fundtion and give it the paths of the mp4 and the mp3

```
convert_mp4_to_mp3("input_mp4", "output_mp3")
```

# you also need to set up the API connection with Mixcloud 

First, go to the Mixcloud API website and set up a new app
https://www.mixcloud.com/developers/

In the bit where you add a link, insert the landing page of your artist page

Next, you need to go to this link:
https://api.mixcloud.com/

Here, you will see the app that you created. Click on the app. 
Now you need to get your client id and also the artist landing page and paste them into this link:
https://www.mixcloud.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI

Approve the request using this link and now your computer and Mixcloud are connected! 

