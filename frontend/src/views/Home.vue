<template>
  <div class="home">
    <h1>Super orgContact</h1>
    <h1 class="display-4">orgContact</h1>
    <h4 class="display-1">orgContact</h4>
    <p class="blue green--text">Get a list of your contacts, group by domain and contacts them</p>

    <!-- Sign in Button -->
    <v-btn 
      elevation="3"
      color="#4285F4"
      class="pl-0 py-5 rounded"
      width="233"
      height="42"
      @click="signIn()"
    >
      <v-img
        lazy-src="@/assets/btn_google_light.svg"        
        src="@/assets/btn_google_light.svg"
         class="mr-4"
      />
      <p class="mb-0 px-2 font-weight-medium text-capitalize white--text">Signin With Google</p>
    </v-btn>
    
  </div>
</template>

<script>
  import {getAuth, GoogleAuthProvider, signInWithPopup} from 'firebase/auth';

  export default {
    name: "Home",
    methods: {
      signIn(){
        const provider = new GoogleAuthProvider();
        provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
        const auth = getAuth();

        signInWithPopup(auth, provider).then(result => {
          const credential = GoogleAuthProvider.credentialFromResult(result);
          const token = credential.accessToken;
          const user = result.user;

          console.log({credential, token, user});
          this.$router.push('/dashboard')
        }).catch((error) => {           
          const errorCode = error.code;
          const errorMessage = error.message;
          // The email of the user's account used.
          const email = error.email;
          // The AuthCredential type that was used.
          const credential = GoogleAuthProvider.credentialFromError(error);
          console.log({errorCode, errorMessage, email, credential})
        })
      }
    }
}     
  
</script>
