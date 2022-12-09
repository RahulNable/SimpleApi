<template>

  <div class="container">
    <h2 class="text-center mt-4 mb-4">
      Convert Excel to HTML Table using JavaScript
    </h2>
    <div class="card">
      <div class="card-header"><b>Select Excel File</b></div>
      <div class="card-body">
        <input type="file" @change="fetchUsers" id="excel_file" />
      </div>
    </div>
    <table class="table table-striped table-bordered">

      <tr v-for="(user, rowindex) in users" :key="rowindex" class="mt-5">

        <td v-for="(data, colindex) in user" :key="colindex" class="mt-5">
          
          {{imagedata[rowindex]}}

        </td>

      </tr>

    </table>

  </div>

</template>

<script>

import axios from 'axios';
import readXlsFile from "read-excel-file";


export default {
  name: "GetPage",
  data() {
    return {
      imagedata: [],
      users: [],
      loading: false,
    };
  },

  methods: {
    async fetchUsers(e) {
      this.loading = true;
      this.users = [];

      readXlsFile(e.target.files[0]).then((rows) => {
        this.users = rows
        console.log('users', this.users);
      })

      await axios
        .get("http://192.168.1.43:9000/file/data/")
        .then((response) => {
          const data = response.data;
          this.imagedata = data.imagedata;
          console.log('imagedata', this.imagedata);
          this.loading = false;
        });

    },

  },

};

</script>

<style>
.fetch-profile {
  display: flex;
  justify-content: center;
  width: 90%;
  padding: 30px;
}

.thead-bg {
  background-color: rgb(221, 220, 220);
}

.btn-users {
  background-color: #000;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.user-table {
  border-collapse: collapse;
  width: 100%;
}

.user-table td,
.user-table th {
  border: 1px solid #ddd;
  padding: 8px;
}

.user-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.user-table tr:hover {
  background-color: #ddd;
}

.user-table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: rgb(221, 220, 220);
  color: rgb(49, 49, 49);
}
</style>