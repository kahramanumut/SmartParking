-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Anamakine: localhost
-- Üretim Zamanı: 31 May 2017, 21:52:56
-- Sunucu sürümü: 5.7.11
-- PHP Sürümü: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `akilliotopark`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `park`
--

CREATE TABLE `park` (
  `ID` int(11) NOT NULL,
  `Durum` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `park`
--

INSERT INTO `park` (`ID`, `Durum`) VALUES
(1, 'B'),
(2, 'B'),
(3, 'B'),
(4, 'D'),
(5, 'D'),
(6, 'B'),
(7, 'B'),
(8, 'B');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
