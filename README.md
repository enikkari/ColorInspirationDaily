Work in progress

Results visible on Instagram [colourinspirationdaily](https://instagram.com/colourinspirationdaily)

[Instagram graph api documentation](https://developers.facebook.com/docs/graph-api)

Posting things to Instagram

To get the necessary permissions set up:
1. Create app for business in Facebook developers 
2. Add Instagram Graph api to app 
3. Add a test user and get the instagram_business_account id (not the same as account id..) [follow instructions](https://developers.facebook.com/docs/instagram-api/getting-started)
    * needs to be a Facebook DEVELOPER account that is connected to a instagram BUSINESS account
4. generate token for test user in 
[Facebook Graph Explorer tool](https://developers.facebook.com/docs/graph-api/explorer/)
    * with persmissions:
    * instagram_basic
    * instagram_content_publish
    * pages_read_engagement OR pages_show_list
5. (exchange short lived token to a long lived token)

[Getting started](https://developers.facebook.com/docs/instagram-api/getting-started)

[More about access tokens](https://developers.facebook.com/docs/pages/access-tokens#page-tasks)

[Content publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#publish-photos)

Note that image / video url needs to be in a publicly available address to that the instagram api can publish it
