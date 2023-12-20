# mushroom_edibility

# water_potability
This repo is created for the projects done for the ML_ZOOMCAMP from data.talks

## Files present
- notebook.ipynb: jupyter notebook file with dataframe ingestion, analysis, EDA, feature selection and ml model hyperparameter tuning
- train.py: python file that was used to create final ml model and dictVectorizer available at model.bin
- model.bin: binary file created with pickle with ml model and dictVectorizer to be used into classification
- predict.py: python file created to generate a flask app to allow usage of model.bin as a webservice.
- predict_test.py: python file created to test the webservice. This can be used for localhost test or cloud test, just chaneg the url.
- Pipfile and Pipfile.lock: files to create a pipenv to execute files and build container.
- Dockerfile: docker configuration file to create containerto be run locally or at cloud.
- mushroom.csv: dataset to be used in case link to original github file repository is removed. This dataset was originated from [link](https://github.com/MainakRepositor/Datasets/tree/master).
  
## Description of the problem
Mushroom hunting, also known as "shrooming" is a growing activiity. Despite being a seemengly simple activity, it can bring many problems since some mushroom varieties are poisonous for us humans.

This lead to the reason for this project, determine based on visual and odor charactewristics if the mushroom is pousonous or not.

This project uses a detaset build based on 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981).

The attributes are the following:



    cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

    cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

    cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

    bruises: bruises=t,no=f

    odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

    gill-attachment: attached=a,descending=d,free=f,notched=n

    gill-spacing: close=c,crowded=w,distant=d

    gill-size: broad=b,narrow=n

    gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

    stalk-shape: enlarging=e,tapering=t

    stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

    stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

    stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

    stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

    stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

    veil-type: partial=p,universal=u

    veil-color: brown=n,orange=o,white=w,yellow=y

    ring-number: none=n,one=o,two=t

    ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

    spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

    population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

    habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d


## How to run project

### Clone project locally
Plase fork the project and create a local clone of the project locally using:

``` git clone <your-repo-url> ``` 

### Start pipenv environent

The files Pipfile and Pipfile.lock conatin the dependencies to execute the code without issues, therefore it is recomended to install and start the virtual environment as following:

- ``` pip install pipenv ``` in case you do not already have if
- ``` pipenv install ```
- From within the directory that have the Pipfile and Pipfile.lock execute the following command in prompt ``` pipenv shell```

### Create model.bin, no need to be executed

This step is not mandatory since we already have the file model available. You can execute the file using the command:
``` python3 train.py```

### Run webservice locally 

It is possible to run the webservice locally using the following command: ``` python3 predict.py```.

In order to locally test the service, uncomment the url from the file predict_test.py for localhost, save it and run the file predict_test.py from a differnt enviroment. Trying to use the same from pipenv will cause an error since it is already running the webservice.

In order to stop the webservice send the command: ``` CTRL + c```.

### Creating a docker image and save it to docker hub

In order to create a docker image, we assume you already have a docker installed in your computer.

To build the image locally execute the following command into the directory with Dockerfile:

``` docker build -t mushroom-edibility-flask .```

Create a docker hub account. This can be easily done using your github account. 

Once logged, create a repository as public with same name as your already created docker image. 

Next a access token need to be created as following:

- Click your username at right top corner,
- Enter Account setting,
- Select Security,
- Click on "Create Access token",
- Populate name and leave it as "Read, write, Delete",
- run the steps prompted to connect your environment to the docker hub.

After we will  create a new image and deploy it to the docker hub using the following commands:

``` docker build -t <your_username>/mushroom-edibility-flask .```
``` docker push <your_username>/mushroom-edibility-flask```

### Deployment to Google Cloud Platform

We assume you already have a GCP account. 

Search for Cloud run service and click create service.

Populate the needed information as following: 

- Container image URL: nireplag/mushroom-edibility-flask
- Service Name: mushroom-edibility
- Ingress Control: All
- Authentication: Allow unauthenticated invocations
- Container port: 9696

It is also recommneded to change the region and Autoscaling feautres as you see fit.
At end of deployment you will have the following:
![image](https://github.com/Nireplag/mushroom_edibility/assets/70478646/3908c399-c0ed-45b7-8afd-6bf73205c836)


### Testing Cloud deployment

The service is already running under the url [https://mushroom-edibility-2rtrkbrwna-uc.a.run.app](https://mushroom-edibility-2rtrkbrwna-uc.a.run.app).

This url can be used into the predict_test.py file with an additional '/predict'. This is already availabe there and the file can be run as the local test, just changing the url commented.

As result of the execution, we will get a json with the payload being passed and the potability probability.

The file after executing will respond the following:
![image](https://github.com/Nireplag/mushroom_edibility/assets/70478646/c11e8d24-2f7d-42eb-a0a7-f4005ec45abd)




