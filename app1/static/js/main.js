
// appoinment form
$("#appoinmentid").validate({
    rules: {
        name: {
            required: true,
            minlength: 3
        },
        email: {
            required: true,
           
        },
        address: {
            required: true,
        },
        date: {
            required: true,
        },
        selectpet: {
            required: true,
        },
        petname: {
            required: true,
        },
        petbreed: {
            required: true,
        },
        petissue: {
            required: true,
        },
        petsex: {
            required: true,
        },
        petage: {
            required: true,
            
        },
        petweight: {
            required: true,
           
        }
    },
    messages: {
        name: {
            minlength: "Name should be at least 3 characters"
        },
        // phonenumber: {
        //     required: "Please enter your Phonenumber."
        // },
        email: {
            required:"The email should be in the format: abc@domain.tld or Enter phone number"
        },
        address: {
            required: "please enter your address."
        },
        date: {
            required: "Please provide a valid Appoinment Date."
        },
        selectpet: {
            required: "Please select a valid pet."
        },
        petname: {
            required: "Please provide your petname."
        },
        petbreed: {
            required: "please enter your pet name."
        },
        petissue: {
            required: "please enter your petproblem."
        },
        petsex: {
            required: "please select your petsex."
        },
        petage: {
            required: "please enter your petage."
        },
        petweight: {
            required: "please enter your petweight"
        }


    }
});



// ending table search

// message 

$("#feedback").validate({
    rules: {
        firstname: {
            required: true,
            minlength: 3
        },
        lastname: {
            required: true,
        },
        email: {
            email:true,
            required: true
        },
        phonenumber: {
            required: true,
            minlength: 10
        },
        message: {
            required: true,
        }
      
    },
    messages: {
        fristname: {
            minlength: "Name should be at least 3 characters"
        },
        lastname: {
            minlength: "Please enter your last name"
        },
        email: {
            email: "",
            required:"The email should be in the format: abc@domain.tld or Enter phone number"
        },
        phonenumber: {
            minlength: "Number should be at least 10 number"
        },
        message: {
            required: "Please write message."
        }
        
    }
    
});


// service booking\
$("#serviceId").validate({
    rules: {
        yname: {
            required: true,
            minlength: 3
        },
        phonenumber: {
            required: true,
            minlength: 10
        },
        email: {
            required: true,
           
        },
        address: {
            required: true,
        },
        date: {
            required: true,
        },
        petname: {
            required: true,
        },
        service: {
            required: true,
        },
        petbreed: {
            required: true,
        },
        petage: {
            required: true,
            
        },
        petweight: {
            required: true,
           
        }
    },
    messages: {
        yname: {
            minlength: "Name should be at least 3 characters"
        },
        phonenumber: {
            required: "Please enter your Phonenumber."
        },
        email: {
            required:"The email should be in the format: abc@domain.tld or Enter phone number"
        },
        address: {
            required: "please enter your address."
        },
        date: {
            required: "Please provide a valid Appoinment Date."
        },
        petname: {
            required: "Please provide your petname."
        },
        service: {
            required: "Please select your service."
        },
        petbreed: {
            required: "please enter your pet name."
        },
        petage: {
            required: "please enter your petage."
        },
        petweight: {
            required: "please enter your petweight"
        }


    }
});

