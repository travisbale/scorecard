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
      }
    }

    stage('Test') {
      steps {
        sh '''
          docker run --rm \
            --env-file /home/env/scorecard/test.env \
            --network=ec2-user_default \
            --entrypoint python scorecard:$IMAGE_TAG -m pytest
        '''
      }
    }

    stage('Deploy') {
      steps {
        // Don't fail the build if the container does not exist
        sh 'docker stop $CONTAINER_NAME || true'
        sh '''
          docker run -d --rm \
            --name $CONTAINER_NAME \
            --env-file /home/env/scorecard/$ENV_FILE \
            --network=ec2-user_default \
            scorecard:$IMAGE_TAG
        '''
      }
    }
  }
}
