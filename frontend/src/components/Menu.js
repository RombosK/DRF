import React from 'react'

const MenuItem = ({menu}) => {
    return (
    <nav>
        <li>
            <a href={menu.url}>{menu.name}</a>
        </li>
    </nav>
    )
}

const MenuList = ({item_menu}) => {
    return (
        <ul className='menu-list'>
            {item_menu.map((menu) => <MenuItem menu={menu} />)}
        </ul>
    )
}

export default MenuList;
