# app

source vevn/bin/activate
pip install -r requirements.txt

# Setup dev environment

```
git clone git@github.com:MovieQuestCY/app.git
cd app/
```

You have to create a ```index.ts``` file in app/frontend/src/secret/ that contains your TMdB v4 API key as follow :

```
export const tmdbToken = "your_token"
```

Then, you can run the dockerfile located in app/

```
docker-compose up -d
```

The env dev will be available at : http://front.dev.neuvy.eu
