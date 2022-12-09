<script>
import { reactive } from 'vue'

export default {
    name: 'App',
    data: function () {
        return {
            // employees: reactive([        // here it also works without reactive
            employees: reactive([
                {
                    name: '',
                    job: '',
                    about: '',
                    another_field: [{
                        tax: '',
                    }]
                }
            ])
        }
    },

    methods: {
        newEmployeeForm() {
            this.employees.push({
                name: '',
                job: '',
                about: '',
                another_field: [{
                    tax: '',
                }]
            })
        },

        add(index) {
            this.employees[index].another_field.push({
                tax: '',
            })
        },

        deleteEmployeeForm(index) {
            this.employees.splice(index, 1)
        },

        submit() {
            console.log(this.employees);
        }
    }
}
</script>

<template>
    <div class="container">This is form 2
        <button class="btn btn-primary mt-5 mb-5" @click="newEmployeeForm">New Employee</button>

        <div class="card mb-3" v-for="(employee, index) in employees">
            <div class="card-body">
                <span class="float-right" style="cursor: pointer;" @click="deleteEmployeeForm(index)">X</span>
                <h4 class="card-title">Add Employee (index: {{ index }})</h4>

                <div class="employee-form">
                    <input type="text" class="form-control mb-2" placeholder="Name" v-model="employee.name">
                    <input type="text" class="form-control mb-2" placeholder="Job" v-model="employee.job">
                    <textarea class="form-control" cols="30" rows="10" placeholder="about"
                        v-model="employee.about"></textarea>

                    <div v-for="(emp, i) in employee.another_field">
                        <h4>Field(index: {{ i }})</h4>

                        <input type="text" class="form-control mb-2" placeholder="Another Field" v-model="emp.tax">

                    </div>
                </div>
            </div>

            <div class="card-body">
                <button class="btn btn-success mt-5 mb-5" id="add_more_fields" @click="add(index)">Add Field</button>
                <!-- <button class="btn btn-danger mt-5 mb-5" id="remove_fields" @click="remove">Remove Field</button> -->
            </div>
        </div>

        <button class="btn btn-success mt-5 mb-5" @click="submit">Submit</button>

    </div>
</template>