<template>
        <div class="container">
                <button class="btn btn-success" @click="get_items">Get Items</button>
                <hr>
                <div class="col-lg-6">
                <ul class="list-group"><Item  v-for="item in items" :item=item :key=item.item_code></Item></ul>
                </div>
        </div>
</template>

<script>
        import ButtonCounter from './ButtonCounter.vue'

        export default {
                name: "ToolRoot",
                data: function () {
                        return {
                                items: [],
                        }
                },
                components: {
                       Item : ButtonCounter
                },
                methods: {
                        get_items() {
                                frappe.xcall('erpnext.selling.page.point_of_sale.point_of_sale.get_items', {
                                        start : 1,
                                        page_length: 100,
                                        price_list: "Standard Selling",
                                        item_group: "All Item Groups",
                                }).then((res) => {
                                        console.log(res.items);
                                        this.items = res.items
                                })
                                
                        },
                }
        }
</script>

<style scoped>
        button {
                margin: 10px;
        }
</style>