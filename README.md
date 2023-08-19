# try-cloud-run-jobs

it may be used as template in the future...

## Build container

```
docker build -t gcr.io/$PROJECT_ID/$IMAGE_NAME .
```

e.g.

```
docker build -t gcr.io/test-cloud-run-as-batch/minimal .
```

## Run app on local

```
docker run try-cloud-run-jobs SUB_COMMAND_OF_MY_APP ARGS
```

e.g.

```
docker run try-cloud-run-jobs create --from-date 2023-08-01 --to-date 2023-08-09
docker run try-cloud-run-jobs delete --from-date 2023-08-01 --to-date 2023-08-09
```

## Deploy

### Set up gcloud

```
gcloud auth login lee.unseo17@gmail.com
gcloud auth configure-docker
gcloud config set project test-cloud-run-as-batch
```

### Deploy

```
gcloud run jobs create MY_CLOUD_RUN_JOBS_NAME --image IMAGE_TAG --args=DOCKER_CMD_OF_MY_APP
```

e.g.

```
gcloud run jobs create create-job --image gcr.io/test-cloud-run-as-batch/minimal --args=create
gcloud run jobs create delete-job --image gcr.io/test-cloud-run-as-batch/minimal --args=delete
```

update deployment

```
gcloud run jobs update create-job --image gcr.io/test-cloud-run-as-batch/minimal --args=create
```

## Run app on cloud

just execute

```
gcloud beta run jobs execute create-job
```

execute with override config

```
gcloud beta run jobs execute create-job --args=create,--from-date,2023-08-09,--to-date,2023-09-09
```
