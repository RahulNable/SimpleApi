<script >
import { ref, reactive, computed } from 'vue';

import readXlsFile from "read-excel-file";
import axios from 'axios';

export default {

  name: 'anything',
  props: ['modelValue'],
  emits: ['update:modelValue'],
  data() {
    return {

      users: [],
      imagesPr: [],
      loading: false,

      files: [{
        filename: '', fileType: '', fileSize: '',
        lastModifiedDate: '',
        uploadedFile: {},
        CurrentIndexView: false,
        viewBtn: "",
        uploadBtn: "",
        excelFiles: [],
      }],

      itemsEx: [],
      filenamelist: [],
    }
  },

  methods: {

    handleFiles(e) {
      const inputValue = e.target.files || e.dataTransfer.files || this.$refs.dropzoneFile.files
      console.log(e.target.files);

      for (let i = 0; i < inputValue.length; i++) {
        const fileItem = inputValue[i]

        console.log("file itmmm=======", fileItem);
        this.files.push(
          { filename: fileItem.name, fileSize: fileItem.size, fileType: fileItem.type, lastModifiedDate: fileItem.lastModifiedDate, uploadedFile: fileItem, CurrentIndexView: false, viewBtn: 'view >', excelFiles: [], uploadBtn: "click here to upload file" })

      }

      console.log(this.files);
      this.$emit('update:modelValue', this.files)

    },




    fetchUsers() {

      this.loading = true;
      axios
        .get("http://192.168.1.43:9000/file/data/")
        .then((response) => {
          const data = response.data;
          console.log(response.data);

          this.users = data.imagedata;
          for (let j = 0; j < this.users.length; j++) {
            this.imagesPr.push({ column: this.users[j].col, rows: this.users[j].row, imagenames: this.users[j].imagename });
          }

          console.log("imgaessss data====", this.users);

          this.loading = false;
        });
    },

    fetchFilenames() {
      this.loading = true;
      axios
        .get("http://192.168.1.43:9000/file/filelist/")
        .then((response) => {
          const data = response.data;
          console.log(response.data);
          this.filenamelist = data.filenames;
          console.log(this.filenamelist);
          this.loading = false;
        });
    },


    fileupload(index) {
      console.log("fileUpload is called")
      this.files[index].uploadBtn = 'uploading...'
      var formData = new FormData();
      formData.append("file", this.files[1].uploadedFile);

      axios.post('http://192.168.1.43:9000/file/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }


      ).then(function () {

        console.log('SUCCESS!!');
        // console.log('uploadbtn=====', this.files[index].viewBtn = "view >");

      },

      )
        .catch(function () {
          console.log('FAILURE!!');
          // this.files[index].uploadBtn = "Faild to upload"

        },
          this.files[index].uploadBtn = 'uploaded'

        );

    },



    subirExcel(index) {




      if (this.files[index].CurrentIndexView == true) {

        this.files[index].CurrentIndexView = false
        this.files[index].viewBtn = "view >"

      } else {


        this.files[index].CurrentIndexView = true
        this.files[index].viewBtn = "close <"
      }

      console.log(this.files[index].uploadedFile);
      console.log(index);


      // const bufferArray = this.files[index].uploadedFile;

      //   const wb = Xlength.read(bufferArray, { type: "buffer" });

      //   console.log("sheet length ========",wb.Sheets)

      //   const wsname = wb.SheetNames[0];



      //   console.log("wsname ================",wsname);


      readXlsFile(this.files[index].uploadedFile, { sheet: 1 }).then((rows) => {
        this.files[index].excelFiles = rows;

        console.log("read excelFiles")
        console.log(rows)
        console.log("loggggg===")

      })

      // const file = xlsx.reader.readFile(this.files[index].uploadedFile)
      // let data = []
      // console.log('i am here',file.Sheets[file.SheetNames[4]]);




      //     const readExcel = (file) => {
      //   const promise = new Promise((resolve, reject) => {
      //     const fileReader = new FileReader();
      //     fileReader.readAsArrayBuffer(this.files[index].uploadedFile);

      //     fileReader.onload = (e) => {
      //      const bufferArray = this.files[index].uploadedFile;

      //       const wb = XLSX.read(bufferArray, { type: "buffer" });

      //       const wsname = wb.SheetNames[0];

      //       // const ws = wb.Sheets[wsname];
      //       this.files[index].excelFiles = wsname;

      //       // const data = XLSX.utils.sheet_to_json(ws);

      //       console.log("length of sheet=====",wsname.length)

      //       resolve(data);
      //     };

      //     fileReader.onerror = (error) => {
      //       reject(error);
      //     };
      //   });

      //   promise.then((d) => {
      //     setItems(d);
      //   });
      // };

    }

  },


}


</script>

<template>

  <div>

    <div class="center">

      <input multiple class="form" id="dropzone-file" type="file" @change="handleFiles"
        placeholder="Drag and Drop to Upload file" />

    </div>
    
    <div class="center">
      <button class="btn btn-primary" @click="fetchFilenames()">Get FileNames</button>
      <table v-if="filenamelist" class="table table-striped table-bordered">
        <tr>
          <div v-for="(file, index) in filenamelist" :key="index">
            <td>{{ file.filename }}</td>
          </div>
        </tr>
      </table>
      <table class="table table-striped table-bordered">
        <tr>
          <th> File Name </th>
          <th> Status </th>
          <th> </th>
          <th> View Data </th>
          <!-- <th> </th>
          <th> </th> -->
        </tr>

        <tr v-for="(file, index) in files" :key="file">

          <td v-if="index > 0">{{ index }}</td>
          <td v-if="index > 0">{{ file.filename }}</td>
          <td v-if="index > 0"> {{ (file.fileSize / 1024).toFixed(2) }}kb </td>
          <td v-if="index > 0"> {{ file.fileType }} </td>

          <!-- <td v-if="index > 0">{{ }} Uploaded </td> -->
          <td v-if="index > 0">{{ }} <button class="btn btn-primary" @click="fileupload(index)">{{
              files[index].uploadBtn
          }}</button>
          </td>
          <td v-if="index > 0"> <button class="btn btn-dark" @click="subirExcel(index); fetchUsers();"> {{
              files[index].viewBtn
          }}</button>
          </td>
          <td>
          <td v-if="index > 0 && this.files[index].CurrentIndexView == true">
            <br>
            <br>
            <table class="table table-striped table-bordered">
              <template v-for="(itemParent, indexP) in files[index].excelFiles" :key="itemParent">
                <tr>
                  <td class="spaceBet" v-for="(itemChild, indexChild) in itemParent" :key="itemChild">
                    {{ itemChild }}
                    <div v-for="(user, indexI) in users" :key="indexI">
                  <td v-if="indexChild == imagesPr[indexI].column && indexP == imagesPr[indexI].rows">
                    <img
                      :src="`http://192.168.1.43:9000/mediafiles/ExtractedExcelfile/xl/media/${imagesPr[indexI].imagenames}`"
                      width="20" height="20">
                  </td>
                <tr v-else></tr>
    </div>
    </td>
    </tr>

    <!-- ///////////////////////////////////// -->
    <!-- <hr> -->
    <!-- <h1> {{ indexP }} : {{ itemParent }}</h1> -->
</template>
</table>
<br>
<br>

</td>
</td>

</tr>
</table>
</div>


</div>

<!-- <button @click="fileupload()">press to post file</button> -->

<!-- <h2> -->
<!-- {{imagesPr[1].row}} -->
<!-- {{ imagesPr }}

  {{ imagesPr.length }}

</h2> -->
<!-- <h2 v-if="this.users[1].row== 1">
    {{imagesPr[1].row}}
    {{users[3]}}
    
  </h2> -->
<!-- <h2>
  {{ users.length }}
</h2> -->
<!-- <h2>
  {{ users }}
</h2> -->
</template>


<style>
.spaceBet {
  margin: 40px;

}

.center {
  text-align: center;
  align-items: center;
  display: flex;
  justify-content: center;

}

.np-progress-container {
  width: 300px;
  height: 20px;
  background: blue;
  border-radius: 6px;
  position: relative;
}

.dragsize {

  height: 400px;
  width: 400px;
  background-color: aqua;
}

.table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  border: 1px solid black;
}

table tr {
  border: 1px solid black;
}

.td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.tr:nth-child(even) {
  background-color: #dddddd;
}

.form {
  display: block;
  padding: 90px;
  height: 200px;
  width: 400px;
  background: #ccc;
  margin: auto;
  margin-top: 40px;
  margin-bottom: 40px;
  text-align: center;
  border-radius: 10px;
  border: 3px black dashed;
  background-color: rgb(84, 131, 181);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

