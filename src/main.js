
import { createApp } from 'vue'
import App from './App.vue'

const getXMLRequestObject = () => {
    const xml = new XMLHttpRequest();
    return xml;
}

export default getXMLRequestObject;
createApp(App).mount('#app')
