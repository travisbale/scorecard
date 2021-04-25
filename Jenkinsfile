pipeline {
  agent any

  environment {
    IMAGE_TAG = "${env.BRANCH_NAME == 'master' ? '0.1' : '0.1-rc'}"
    ENV_FILE = "${env.BRANCH_NAME == 'master' ? 'prod.env' : 'staging.env'}"
    CONTAINER_NAME = "${env.BRANCH_NAME == 'master' ? 'scorecard' : 'scorecard-rc'}"
    KEY_DIR = "${env.BRANCH_NAME == 'master' ? 'prod' : 'staging'}"
  }

  stages {
    stage('Build') {
      steps {
        sh 'mkdir -p keys'
        sh 'cp /home/keys/$KEY_DIR/heimdall.pub keys'
        sh 'docker build -t scorecard:$IMAGE_TAG .'
        sh 'docker build -t scorecard-test:$IMAGE_TAG --target test .'
      }
    }

    stage('Test') {
      steps {
        sh '''
          docker run --rm \
            --env-file /home/env/scorecard/test.env \
            --network=ec2-user_default \
            scorecard-test:$IMAGE_TAG
        '''
      }
    }

    stage('Deploy') {
      steps {
        // Don't fail the build if the container does not exist
        sh 'docker stop $CONTAINER_NAME || true'
        sh 'docker rm $CONTAINER_NAME || true'
        sh '''
          docker run -d \
            --restart always \
            --log-opt max-size=10m --log-opt max-file=3 \
            --name $CONTAINER_NAME \
            --env-file /home/env/scorecard/$ENV_FILE \
            --network=ec2-user_default \
            scorecard:$IMAGE_TAG
        '''
      }
    }
  }
}
