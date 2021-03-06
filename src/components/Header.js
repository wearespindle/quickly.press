import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { logo } from './images';
import './Header.css';

class Header extends Component {
  render() {
    return (
      <div>
      <div className="columns is-gapless is-marginless header-colorbar">
        <div className="column"></div>
        <div className="column"></div>
        <div className="column"></div>
        <div className="column"></div>
      </div>
      <nav className="nav">
        <div className="container">
          <div className="nav-left">
            <Link className="nav-item is-paddingless" to="/">
              <img src={logo} alt=""/>
            </Link>
          </div>
          <span className="nav-toggle">
            <span></span>
            <span></span>
            <span></span>
          </span>
          <div className="nav-right nav-menu">
            <Link to="/settings" className="nav-item is-tab">
              <figure className="image is-16x16" style={{ marginRight: '8px'}}>
                <img src="https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/12079190_10207381455322317_5529711437017744926_n.jpg?oh=685f5286ecf9f0665638a4f9926206ad&oe=59BAB1C9" alt="User"/>
              </figure>
              John D.
            </Link>
            <a className="nav-item is-tab">Log out</a>
          </div>
        </div>
      </nav>
    </div>
    );
  }
}

export default Header;
