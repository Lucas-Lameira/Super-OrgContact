<template>
  <v-btn @click="logOut()">
    SignOut
  </v-btn>
</template>

<script>
  import {getAuth, signOut} from 'firebase/auth';
  export default {
    name: "Dashboard",
    methods: {
    
    logOut() {

      const auth = getAuth();
      signOut(auth).then(() => {
        console.log("logged out")
        this.$router.push('/')
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>