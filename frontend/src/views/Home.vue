<template>
  <!-- <div class="home deep-purple d-flex justify-space-between align-center"> -->
  <div>
    <v-container fluid >
      <v-row class="fillHeight" justify="center"> 

        <v-col align-self="center" xs="6" sm="8" md="4" lg="5" xl="4">
          <section>
            <h1 class="display-3 font-weight-bold white--text">
              Super OrgContact
            </h1>
            <p class="white--text my-8">
              A Super OrgContact  ajuda você a listar e agrupar seus contatos. Cadastre-se com o google e começe a usar o nosso web site! 
            </p>

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
          </section>
        </v-col>
        <!-- homepage image -->     
        <v-col 
          align-self="end" 
          class="d-none d-md-block py-0" md="4" lg="4" xl="4">
          <v-img
            lazy-src="@/assets/people.svg"
            contain
            max-height="100vh"
            src="@/assets/people.svg"
            class="hidden-sm-and-down"
          />   
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>
  import {getAuth, GoogleAuthProvider, signInWithPopup} from 'firebase/auth';
  import {firebaseApp} from '../services/firebaseService';
  
  export default {
    name: "Home",
    methods: {
      async signIn(){
        try{
          const provider = new GoogleAuthProvider();
          provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
          const auth = getAuth(firebaseApp);
          /* eslint-disable */
          const result = await signInWithPopup(auth, provider);
          const user = result.user

          
        }catch(error){
          console.log(error)
        }
      },
    }
}     
  
</script>


<style scoped>
.fillHeight{
  height: 100vh;
}
</style>