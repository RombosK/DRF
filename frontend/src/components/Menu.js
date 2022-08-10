import React from 'react'

const MenuItem = ({menu}) => {
    return (

        <li>
            <a href={menu.url}>{menu.name}</a>
        </li>

    )
}

const MenuList = ({item_menu}) => {
    return (
        <ul className='mainmenu'>
            {item_menu.map((menu) => <MenuItem menu={menu} />)}
        </ul>
    )
}

export default MenuList;



