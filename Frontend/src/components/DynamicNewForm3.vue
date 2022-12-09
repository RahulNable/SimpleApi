<template>
    <div class="container mt-4">
        <div class="row">
            <div class="col-6" v-if="button">
                <button id="addcustomer" @click="addCustomer" type="button" class="btn btn-outline-primary">
                    Add Customer
                </button>
            </div>
            <div class="col-6" v-if="!button && listitems">
                <!-- <div style="width: 10cm; box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;">
                    <input class="form-control mr-sm-2" type="search" placeholder="type a customer name"
                        aria-label="Search" style="width: 10cm;">

                    <div class="mt-3" style="overflow:scroll; max-height:200px; width: 10cm;">
                        <div class="list-group">

                            <div class="list-group-item list-group-item-action list-group-item-primary" @click="selectCustomer">
                                <h5>Rahul</h5>
                                <p>He is a developer</p>
                            </div>
                            <div class="list-group-item list-group-item-action list-group-item-primary">
                                <h5>Rahul</h5>
                                <p>He is a developer</p>
                            </div>
                            <div class="list-group-item list-group-item-action list-group-item-primary">
                                <h5>Rahul</h5>
                                <p>He is a developer</p>
                            </div>
                            <div class="list-group-item list-group-item-action list-group-item-primary">
                                <h5>Rahul</h5>
                                <p>He is a developer</p>
                            </div>


                        </div>
                    </div>
                </div> -->
                <select name="selectCustomer" id="selectCustomerid" @change="selectCustomer" style="width: 200px;">
                    <option>Select an option</option>
                    <option value="Rahul">Rahul</option>
                    <option value="Aman">Aman</option>
                    <option value="Yash">Yash</option>
                    <option value="Rakesh">Rakesh</option>
                </select>
            </div>
            <div class="col-6" v-if="!button && !listitems && customer_name">
                <h1>{{this.selectedCustomer}}</h1>
            </div>
            <!-- <h3>Items{{items}}</h3> -->

            <div class="col">
                <div class="row">
                    <div class="col-5"></div>
                    <div class="col p-3">
                        <label htmlFor="invoicenumber" style="float: right;">Invoice number</label>
                    </div>
                    <div class="col p-3">
                        <input class="form-control" type="text" name="invoicenumber" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-5"></div>

                    <div class="col p-3">
                        <label htmlFor="posonumber" style="float: right;">PO SO number</label>
                    </div>
                    <div class="col p-3">
                        <input class="form-control" type="text" name="posonumber" />
                    </div>
                </div>


                <div class="row">
                    <div class="col-5"></div>
                    <div class="col p-3">
                        <label htmlFor="invoicedate" style="float: right;">Invoice Date</label>
                    </div>
                    <div class="col p-3">
                        <input type="date" name="invoicedate" data-date-inline-picker="true" />
                    </div>
                    <!-- <div class="col"></div> -->
                </div>

                <div class="row">
                    <div class="col-5"></div>
                    <div class="col p-3">
                        <label htmlFor="paymentdue" style="float: right;">Payment Due</label>
                    </div>
                    <div class="col p-3">
                        <input type="date" name="paymentdue" data-date-inline-picker="true" />
                        <p>On Receipt</p>
                    </div>
                </div>
            </div>

        </div>


        <div class="row">
            <div class="col-8"><b>Items</b> </div>
            <div class="col-1"><b>Quantity</b> </div>
            <div class="col"><b>Price</b></div>
            <div class="col"><b>Amount</b></div>
        </div>

        <div class="card mt-3" v-for="(item, index) in items" :key="item" >
            <div>
                <div class="mt-2">
                    <div class="col">
                        <span class="float-right" style="cursor: pointer;" @click="deleteItemForm(index)">X</span>
                    </div>
                    <div class="row">
                        <div class="col-2">
                            <h5>{{item.itemname}}</h5>
                        </div>
                        <div class="col-5">
                            <textarea type="text" rows="4" class="form-control mb-2"
                                v-model="item.desc">jalkjf</textarea>
                        </div>
                        <div class="col-1"></div>
                        <div class="col-1">
                            <input type="text" class="form-control mb-2" v-model="item.quantity">
                        </div>
                        <div class="col-1">
                            <input type="text" class="form-control mb-2" v-model="item.price">
                        </div>
                    </div>

                    <button @click="dataapi">add data</button>

                    <div v-for="(itm, i) in item.another_field" :key="itm">
                        <div class="row">
                            <div class="col-8"></div>
                            <div class="col-2">
                                <input type="text" class="form-control mb-2" placeholder="tax" v-model="itm.tax">
                            </div>
                            <div class="col">
                                <span class="float-right" style="cursor: pointer;"
                                    @click="deleteItemField(index, i)">X</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card-body">
                <button class="btn btn-success mt-5 mb-5" id="add_more_fields" @click="addtax(index)">Add
                    Tax</button>
            </div>
        </div>

        <button class="btn btn-primary mt-5 mb-5" @click="newItemForm">
         <b>+</b> Add an Item</button>

        <!-- <button class="btn btn-success mt-5 mb-5" @click="submit">Submit</button> -->

        <div class="row">
            <div class="col-8"></div>
            <div class="col-1"></div>
            <div class="col">Sub Total</div>
            <div class="col">{{ this.q * this.price }}</div>
        </div>
        <br>
        <div class="row" v-if="showdiscount">
            <div class="col-3">Discount</div>
            <div class="col-5"><input class="form-control" type="text" name="desc" placeholder="Description"></div>
            <div class="col-1"><input class="form-control" name="disvalue" placeholder="value"></div>
            <div class="col-1">
                <select class="custom-select">
                    <option selected value="1">One</option>
                    <option value="2">Two</option>
                </select>
            </div>
        </div>
        <div class="row" v-if="!showdiscount">
            <button class="btn btn-primary mt-5 mb-5" @click="addDiscount">+ Add Discount</button>
        </div>

    </div>
</template>

<script>
import { reactive } from 'vue'

export default {
    name: 'App',
    data: function () {
        return {
            q: 1,
            price: 100,

            items: reactive([
            ]),

            discount: ([]),
            button: true,
            listitems: false,
            selectedCustomer: '',
            customer_name: '',
            showdiscount: false,
        }
    },

    methods: {
        newItemForm() {
            this.items.push({
                itemname: '',
                desc: '',
                quantity: '',
                price: '',
                amount: '',
                another_field: []
            })
        },

        dataapi(){
            this.items[0].itemname = 'item1'
            this.items[0].desc = 'item1desc'
            this.items[0].quantity = 3
            this.items[0].price = 300

            this.items[1].itemname = 'item2'
            this.items[1].desc = 'item2desc'
            this.items[1].quantity = 2
            this.items[1].price = 200
        },

        addDiscount() {
            this.discount.push({
                description: '',
                value: 10,
                unit: '',
            })
        },

        addtax(index) {
            this.items[index].another_field.push({
                tax: '',
            })
        },

        deleteItemForm(index) {
            this.item.splice(index, 1)
        },

        deleteItemField(index, i) {
            this.item[index].another_field.splice(i, 1)
        },

        addCustomer() {
            this.button = false
            this.listitems = true
        },

        selectCustomer() {
            console.log(document.getElementById("selectCustomerid").value);
            this.listitems = false
            this.selectedCustomer = document.getElementById("selectCustomerid").value
            this.customer_name = true
        },

        submit() {
            console.log(this.item);
        }
    },

}
</script>

<style>
#addcustomer {
    padding: 70px 100px 70px 100px;
}
</style>