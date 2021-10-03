<template>
<!-- further buttons in popup -->
<div>
  <v-btn fab small class="deep-purple">
      <v-icon small color="white">
        mdi-phone
      </v-icon>
    </v-btn>

     <v-btn icon large class="deep-purple">
      <v-icon color="white">
        mdi-email
      </v-icon>
    </v-btn>
</div>
</template>

<script>
export default {
   name: 'Button',
   data(){
      return {
         /* code */
      }
   }
}
</script>