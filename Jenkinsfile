pipeline {
  agent any
  stages {
    stage('get code') {
      steps {
        git(url: 'https://github.com/chrisdadswell/catikins.git', branch: 'master')
      }
    }
  }
}