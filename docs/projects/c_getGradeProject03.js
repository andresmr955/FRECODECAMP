
function getGrade(score) {
    var scoregradex = ""
        if(score == 100){
          scoregradex = "A++";
          return scoregradex
        }else if(score >= 90 && score <= 99){
          scoregradex = "A"
          return scoregradex
        }else if(score >= 80 && score <= 89){
          scoregradex = "B";
          return scoregradex
        }else if(score >= 70 && score <= 79){
          scoregradex = "C";
          return scoregradex
        }else if(score >= 60 && score <= 69){
          scoregradex = "D";
          return scoregradex
        }else if(score >= 0 && score <= 59){
          scoregradex = "F";
          return scoregradex}
    }
    
    console.log(getGrade(96));
    console.log(getGrade(82));
    console.log(getGrade(56));