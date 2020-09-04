<template>
        
                <a @click="show_info = !show_info" class="list-group-item" :class="{activate: show_info}">
                        <span class="badge">{{ item.actual_qty }} {{ item.actual_qty ? item.stock_uom : ''}}</span>
                        {{ item.item_code}}
                
                <div v-if="show_info" class="panel panel-default">
                        <div class="panel-body">
                        Price List: {{ item.price_list_rate }} {{ item.currency }}
                        </div>
                        <div class="panel-footer">Name: {{ item.item_name }}</div>
                </div>
                </a>
        
</template>

<script>
        export default {
                props: ['item'],
                data() {
                        return {
                                show_info : false
                        }
                },
        }
</script>

<style scoped>
        .panel {
                margin-top: 10px;
        }
        .activate {
                background-color: lightgrey;
        }
</style>