// search key 

// function myFunction() {
//     // Declare variables
//     var input, filter, table, tr, td, i, txtValue;
//     input = document.getElementById("myInput");
//     filter = input.value.toUpperCase();
//     table = document.getElementById("myTable");
//     tr = table.getElementsByTagName("tr");
  
//     // Loop through all table rows, and hide those who don't match the search query
//     for (i = 0; i < tr.length; i++) {
//       td = tr[i].getElementsByTagName("td")[0];
//       if (td) {
//         txtValue = td.textContent || td.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//           tr[i].style.display = "";
//         } else {
//           tr[i].style.display = "none";
//         }
//       }
//     }
//   }



// end search key

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
