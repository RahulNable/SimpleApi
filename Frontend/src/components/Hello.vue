<script >
import { ref, reactive, computed } from 'vue';

import readXlsFile from "read-excel-file";

export default {

  name: 'anything',
  props: ['modelValue'],
  emits: ['update:modelValue'],
  data() {

    return {

      data: null,

      files: [{
        filename: '', fileType: '', fileSize: '',

        lastModifiedDate: '',
        uploadedFile: {},

        CurrentIndexView: false,
        viewBtn: "",
        excelFiles: [],
        images: {}
      }],

      itemsEx: [],
    }
  },

  methods: {


    handleFiles(e) {

      const inputValue = e.target.files || e.dataTransfer.files || this.$refs.dropzoneFile.files
      console.log(e.target.files);

      for (let i = 0; i < inputValue.length; i++) {
        const fileItem = inputValue[i]
        this.files.push(
          { filename: fileItem.name, fileSize: fileItem.size, fileType: fileItem.type, lastModifiedDate: fileItem.lastModifiedDate, uploadedFile: fileItem, CurrentIndexView: false, viewBtn: 'view >', excelFiles: [], })




      }

      console.log(this.files);
      console.log(this.files[1].uploadedFile)
      this.$emit('update:modelValue', this.files)




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
      // console.log(this.files[1]);

      // const input = document.getElementById("archiveExcel");

      readXlsFile(this.files[index].uploadedFile).then((rows) => {
        console.log('rows', rows.files);
        this.files[index].excelFiles = rows;



        console.log("read excelFiles")
        console.log(rows)


        console.log("loggggg===")
        console.log(this.files[index].uploadedFile)



      })

    }





  },
  computed: {

  }






}


</script>

<template>

  <div>

    <div class="center">
      <!-- <input type="file" id="dropzone-file" ref="dropzoneFile" @change="handleFiles" class="center"> -->

      <input multiple class="form" id="dropzone-file" type="file" @change="handleFiles"
        placeholder="Drag and Drop to Upload file" />


    </div>









    <div class="center">


      <table class="tbl">

        <tr>
          <th>S.N.</th>
          <th> File Name </th>
          <th> Size </th>
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
          <td v-if="index > 0">{{ }} Uploaded </td>
          <td v-if="index > 0"> <button @click="subirExcel(index)"> {{ files[index].viewBtn }}</button> </td>



          <td>

          <td v-if="index > 0 && this.files[index].CurrentIndexView == true">

            <br>
            <br>
            <table>
              <template v-for="(itemParent, indexP) in files[index].excelFiles" :key="itemParent">
                <h1>{{ itemParent[15] }} {{ indexP }}</h1>

                <tr>

                  <td class="spaceBet" v-for="(itemChild, indexChild) in itemParent" :key="itemChild">
                    {{ itemChild }}


                  </td>
                </tr>
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







</template>


<style
>
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
  height: 400px;
  width: 400px;
  background: #ccc;
  margin: auto;
  margin-top: 40px;
  text-align: center;
  line-height: 400px;
  border-radius: 4px;
  background-color: blue;
  display: flex;
  justify-content: center;
  align-items: center;

}
</style>

