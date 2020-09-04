<template>
        <li class="list-group-item">
                <span class="badge">{{ item.price_list_rate }}</span>
                {{ item.item_code}}
        </li>
</template>

<script>
        export default {
                props: ['item'],
        }
</script>