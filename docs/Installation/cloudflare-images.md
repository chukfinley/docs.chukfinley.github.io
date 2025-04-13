### Cloudflare Images

Upload script
```
#!/bin/bash
# upload_image.sh
#
# Usage: ./upload_image.sh path/to/image.jpg
#
# This script uploads an image to Cloudflare Images and prints out the image URL.

# Replace these with your configuration values.
TOKEN=""
ACCOUNT_ID=""
API_URL="https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/images/v1"

if [ $# -ne 1 ]; then
  echo "Usage: $0 image_path"
  exit 1
fi

IMAGE_PATH="$1"

if [ ! -f "$IMAGE_PATH" ]; then
  echo "Error: File does not exist: $IMAGE_PATH"
  exit 1
fi

response=$(curl -s -X POST -F file=@"$IMAGE_PATH" \
  -H "Authorization: Bearer ${TOKEN}" \
  "${API_URL}")

# Use 'jq' to parse the JSON response if installed.
if command -v jq >/dev/null 2>&1; then
  url=$(echo "$response" | jq -r '.result.variants[0]')
  echo "Image URL: $url"
else
  echo "Response:"
  echo "$response"
  echo "Consider installing jq (https://stedolan.github.io/jq/) for better JSON output."
fi
```

Setting Varinates My Varients are:
![Image](https://imagedelivery.net/2cV7rtGc2GHA56_rfCQmOg/35b3aced-2348-40c6-72b6-0d990f8ca900/4320p)

the one i have set are

p | pixels
- | -
1080p | 1920 x 1080
1440p | 2560 x 1440
2160p | 3840 x 2160
2880p | 5120 x 2880
4320p | 7680 x 4320
720p | 1280 x 720
max | 20000 x 20000


i have set the max to 20000 x 20000 just in case .
i uploded the image above with the script and cloudflre auto returned 4320p i dont know whay because the image is 824 x 847 so 1080p is fine it probably uses the biggest resoltuin that is not 2 big like 20000 x 20000


### Generating an Api Token

- Got To Profile on the right top.
- Than go to API Tokens
- Click Create New.
- Click on Get started at Custom token
- Give it a Name Like images
- At Permissions select the item Cloudflare Images
- also selct edit if you want to upload images via that token
- you can leave Account Resources as it is
- on ip filtering set it to "Is not in" and set the ip to 1.1.1.1 if you want to allow all ips
- Now press Continue to summary
- Copy the api TOKEN
- Done!
