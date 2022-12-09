<script>

import readXlsFile from "read-excel-file";
import axios from 'axios';

export default {

    name: 'anything',
    props: ['modelValue'],

    data() {
        return {
            filenamelist: [],
            ViewFileData: "Select uploaded File",
            ExcelData: [],
            Image: [],
            fileItem: []
        }
    },

    beforeMount() {
        this.onPageLoad();
    },


    methods: {
        onPageLoad() {
            console.log('called before mount----->')
            axios
                .get("http://127.0.0.1:8000/file/filelist/")
                .then((response) => {
                    console.log(response.data);
                    this.filenamelist = response.data.filenames;
                    console.log("filenames=======", this.filenamelist);
                });
        },

        handleFiles(e) {

            const inputValue = e.target.files || e.dataTransfer.files || this.$refs.dropzoneFile.files
            console.log("e.target.files====", e.target.files);
            this.fileItem = e.target.files
            var formData = new FormData();
            console.log("filename========", this.fileItem[0].name)
            // var imagefile = document.querySelector('#file');
            formData.append("file", e.target.files[0]);
            axios.post('http://127.0.0.1:8000/file/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(() => {
                console.log('SUCCESS!!');
                this.onPageLoad();
            }).catch(() => {
                console.log('FAILURE!!');
            },
            );
        },

        refresh() {
            window.location.reload();
            console.log("calleeed");
            // window.location = window.location.href;
        },

        FileViewer(index) {

            fetch("http://127.0.0.1:8000/mediafiles/" + this.filenamelist[index].filename)
                .then(response => response.blob())
                .then(blob => readXlsFile(blob,
                    // { sheet: 4 }
                ))
                .then((rows) => {
                    console.log("rows====", rows);
                    this.ExcelData = rows
                    console.log("ExcelData====", this.ExcelData);
                })

            axios.post('http://127.0.0.1:8000/file/data/', {
                "filename": this.filenamelist[index].filename
            })
                .then((response) => {
                    console.log('response=====', response.data.imagedata);
                    this.Image = response.data.imagedata;
                    console.log("imgaes data====", this.Image);
                    console.log("imgaes cell ====", this.Image[0].col);
                    console.log("FileName cell ====", this.filenamelist[index].filename);
                })
                .catch((err) => {
                    console.log('FAILURE!!=========', err);
                });
        },
    }
}


</script>

<template>

    <br>
    <br>

    <div class="center">
        <input class="form" id="dropzone-file" type="file" @change="handleFiles"
            placeholder="Drag and Drop to Upload file"
            accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel" />
    </div>

    <br>
    <br>

    <div class="center">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">
                {{ ViewFileData }}
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
                <div v-for="(file, index) in filenamelist" :key="file">

                    <button class="dropdown-item" type="button"
                        @click="ViewFileData = file.filename, FileViewer(index)">
                        {{ file.filename }} 
                        <!-- {{ index }} -->
                    </button>
                </div>
            </div>
        </div>
    </div>

    <br>


    <div class="center">
        <table class="table table-striped table-bordered">
            <template v-for="(itemParent, indexP) in ExcelData" :key="itemParent">
                <tr>
                    <td class="spaceBet" v-for="(itemChild, indexChild) in itemParent" :key="itemChild">
                        {{ itemChild }}

                        <div v-for="(user, indexI) in Image" :key="user">
                            <div v-if="indexChild == Image[indexI].col && indexP == Image[indexI].row">
                                <img
                                    :src="`http://127.0.0.1:8000/mediafiles/ExtractedExcelfile/xl/media/${Image[indexI].imagename}`">
                            </div>
                        </div>
                    </td>
                </tr>
            </template>
        </table>
    </div>


</template>

<style>
.center {
    text-align: center;
    align-items: center;
    display: flex;
    justify-content: center;
}

.form {
    display: block;
    padding: 90px;
    height: 200px;
    width: 400px;
    background: #ccc;
    /* background: linear-gradient(to right, #000000 10%, #808080 100%); */
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

