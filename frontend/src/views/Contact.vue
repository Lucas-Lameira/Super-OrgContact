<template>
<div class="contact">
  <nav >
    <v-app-bar dark color="deep-purple lighten-1" >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      
      <v-toolbar-title>
        <span class="white--text font-weight-medium">Super OrgContact</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn 
        elevation="5" 
        large  
        color="green lighten-1 ma-2"
        @click="logOut()"
      >
        <v-icon left>mdi-logout-variant</v-icon>
        <span class="white--text font-weight-regular text-capitalize" >Sign Out</span>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <template v-slot:prepend >
        <v-list-item two-line class="deep-purple white--text">
          <v-list-item-avatar>
            <img :src=user.photoURL>
          </v-list-item-avatar>

          <v-list-item-content >
            <v-list-item-title>{{ user.displayName}}</v-list-item-title>
            <v-list-item-subtitle class="grey--text darken-1 text--lighten-1">Signed In</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in itemss"
          :key="item.title"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title ? item.title: 'No phone number' }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>

  <v-container fluid>
    <v-row 
      align="center"
      justify="center"
      justify-lg="end"
      class="fillHeight"
    >
      
      <v-col sm="12" md="5" lg="7" xl="6">
        <!-- contact list section -->
        <v-list three-line class="overflow rounded-lg" subheader>
          <v-subheader>Contatos</v-subheader>        
          <v-list-item v-for="item in contactList" :key="item.title">

            <v-list-item>
              <v-list-item-avatar>
                <v-img :src="item.photo"></v-img>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title v-html="item.name"></v-list-item-title>
                <v-list-item-subtitle v-html="item.phone"></v-list-item-subtitle>
                <v-divider v-divider></v-divider>
              </v-list-item-content>
            </v-list-item>
          </v-list-item>
        </v-list>
      </v-col>

      
      <!-- girl loggin at the list image -->
      <v-col align-self="end" md="5" lg="4" xl="4" class="d-none d-md-block" > 
        <v-img
          lazy-src="@/assets/girl.svg"
          contain
          min-height="500"
          max-height="800"
          src="@/assets/girl.svg"
        />
      </v-col>

    </v-row>
  </v-container>
</div>
</template>

<script>
  import axios from 'axios'
  import {firebaseApp} from '../services/firebaseService';
  import {getAuth, signOut} from 'firebase/auth';
  import { getDatabase, ref, child, get } from "firebase/database";

  const auth = getAuth(firebaseApp)
  
  export default {
    name: "Contact",
    async created(){
      const user = auth.currentUser;
      const {email, displayName, phoneNumber, photoURL} = user;
      this.user = {email, displayName, phoneNumber, photoURL}
      
      try{
        const dbRef = ref(getDatabase());
        const snapshot = await get(child(dbRef, `users/${user.uid}`));

        if (!snapshot.exists()){
          throw new Error('No data available');
        } 

        let {credentialAccessToken} = snapshot.val();

        const userAccessToken = user.getIdToken();
        const userRefreshToken = user.refreshToken;

        const response = await axios.post('http://127.0.0.1:5000/', "teste", {
          headers: {
            'accessToken':  userAccessToken,
            'refreshToken': userRefreshToken,
            'token': credentialAccessToken
          }
        })

        this.contactList = response.data;
      }catch(error) {
        console.error(error);
      };
    },
    data(){
      return {
        isLoggedIn: false,
        drawer: false,
        user: null,
        itemss: [
          { title: auth.currentUser.email, icon: 'mdi-at' },
          { title: auth.currentUser.phoneNumber, icon: 'mdi-cellphone-settings'},
        ],
        contactList: []
      }
    },
    methods: {
    async logOut() {
      try{
        await signOut(auth);
        console.log("logged out");
        this.$router.push("/");
      }catch(error){
        console.log(error);
      }
    },
  }
}
</script>

<style>
.fillHeight{
  height: calc(100vh - 80px);
}

.overflow{
  overflow-y: scroll;
  scroll-behavior: smooth;
  max-height: 400px;
  box-sizing: content-box;
  padding-right: 17px;
}

::-webkit-scrollbar {
    width: 0;
}
</style>