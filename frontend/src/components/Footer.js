import React from 'react'


const FooterItem = ({footer}) => {
    return (

        <li>
            <a href={footer.url}>{footer.name}</a>
        </li>

    )
}

const FooterList = ({item_footer}) => {
    return (
        <ul className='panel-footer'>
            {item_footer.map((footer) => <FooterItem footer={footer} />)}
        </ul>
    )
}

export default FooterList;
