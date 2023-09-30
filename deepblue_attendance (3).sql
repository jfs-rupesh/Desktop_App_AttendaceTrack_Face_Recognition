-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jan 10, 2017 at 11:33 AM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `deepblue_attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `admin_username` varchar(50) NOT NULL,
  `admin_password` varchar(50) NOT NULL,
  `admin_email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `admin_username`, `admin_password`, `admin_email`) VALUES
(1, 'ngo', 'deepblue', '');

-- --------------------------------------------------------

--
-- Table structure for table `attendence_demo`
--

CREATE TABLE `attendence_demo` (
  `aid` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `attendance` varchar(50) NOT NULL,
  `day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendence_demo`
--

INSERT INTO `attendence_demo` (`aid`, `student_id`, `attendance`, `day`) VALUES
(1, 4, 'PRESENT', 1),
(2, 4, 'ABSENT', 2),
(3, 5, 'PRESENT', 1),
(4, 5, 'PRESENT', 2);

-- --------------------------------------------------------

--
-- Table structure for table `attendence_demoreturns`
--

CREATE TABLE `attendence_demoreturns` (
  `aid` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `attendance` varchar(50) NOT NULL,
  `day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendence_demoreturns`
--

INSERT INTO `attendence_demoreturns` (`aid`, `student_id`, `attendance`, `day`) VALUES
(1, 4, 'PRESENT', 1);

-- --------------------------------------------------------

--
-- Table structure for table `enrolement`
--

CREATE TABLE `enrolement` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `enrolement`
--

INSERT INTO `enrolement` (`id`, `student_id`, `event_id`) VALUES
(1, 4, 10),
(2, 5, 10),
(3, 4, 11),
(4, 5, 11);

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(11) NOT NULL,
  `heading` varchar(50) NOT NULL,
  `details` varchar(10000) NOT NULL,
  `event_date` date NOT NULL,
  `duration` int(11) NOT NULL,
  `felicitator_id` varchar(50) NOT NULL,
  `felicitator2_id` varchar(50) DEFAULT NULL,
  `felicitator3_id` varchar(50) DEFAULT NULL,
  `address` varchar(500) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pincode` int(11) NOT NULL,
  `telephone` bigint(20) DEFAULT NULL,
  `mobile` bigint(20) DEFAULT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`id`, `heading`, `details`, `event_date`, `duration`, `felicitator_id`, `felicitator2_id`, `felicitator3_id`, `address`, `city`, `state`, `pincode`, `telephone`, `mobile`, `latitude`, `longitude`) VALUES
(10, 'demo', 'Somaiya Ayurvihar Complex, Eastern Express Highway, Near Everard Nagar, Sion East, Sion, Mumbai', '2016-11-05', 2, '', 'Aniket', '', 'Silicon Tower Sec-30 Vashi', 'Navi Mumbai', 'Maharashtra', 410206, 8080672062, 8080672062, 19.0661009, 73.0036753),
(11, 'demoreturns', 'aaa', '2016-12-15', 1, '', NULL, NULL, '', '', '', 0, NULL, NULL, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `felicitator`
--

CREATE TABLE `felicitator` (
  `id` int(11) NOT NULL,
  `felicitator_name` varchar(50) NOT NULL,
  `felicitator_middlename` varchar(50) NOT NULL,
  `felicitator_lastname` varchar(50) NOT NULL,
  `felicitator_image` varchar(500) NOT NULL,
  `felicitator_og_image` varchar(500) NOT NULL,
  `felicitator_email` varchar(50) NOT NULL,
  `felicitator_username` varchar(50) NOT NULL,
  `felicitator_password` varchar(50) NOT NULL,
  `felicitator_address` varchar(50) NOT NULL,
  `felicitator_city` varchar(50) NOT NULL,
  `felicitator_pincode` int(11) NOT NULL,
  `felicitator_state` varchar(50) NOT NULL,
  `felicitator_uid` bigint(20) NOT NULL,
  `felicitator_phone` bigint(20) DEFAULT NULL,
  `felicitator_mobile` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `felicitator`
--

INSERT INTO `felicitator` (`id`, `felicitator_name`, `felicitator_middlename`, `felicitator_lastname`, `felicitator_image`, `felicitator_og_image`, `felicitator_email`, `felicitator_username`, `felicitator_password`, `felicitator_address`, `felicitator_city`, `felicitator_pincode`, `felicitator_state`, `felicitator_uid`, `felicitator_phone`, `felicitator_mobile`) VALUES
(2, 'kk', 'nnn', 'kk', '', '', 'mmm', 'Aniket', '06061997', 'nnn', 'nnn', 4, 'nnjjn', 5, 6, 7);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `student_name` varchar(50) NOT NULL,
  `student_middlename` varchar(50) NOT NULL,
  `student_lastname` varchar(50) NOT NULL,
  `student_og_image` varchar(50) NOT NULL,
  `student_crop_image` varchar(50) NOT NULL,
  `student_email` varchar(50) NOT NULL,
  `student_username` varchar(50) NOT NULL,
  `student_address` varchar(50) NOT NULL,
  `student_city` varchar(50) NOT NULL,
  `student_pincode` int(11) NOT NULL,
  `student_state` varchar(50) NOT NULL,
  `student_uid` bigint(20) NOT NULL,
  `student_phone` bigint(20) DEFAULT NULL,
  `student_mobile` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `student_name`, `student_middlename`, `student_lastname`, `student_og_image`, `student_crop_image`, `student_email`, `student_username`, `student_address`, `student_city`, `student_pincode`, `student_state`, `student_uid`, `student_phone`, `student_mobile`) VALUES
(4, 'Yashica', 'Ashutosh', 'Thakkar', 'images/98956.jpg', 'images/989562.jpg', 'yashit@gmail.com', 'yashi_t', 'Niharika Niwas Sec-23 Airoli', 'Navi Mumbai', 410220, 'Maharashtra', 98956, 9892579113, 9892579113),
(5, 'aniket', 'deopriya', 'bharti', '', '', 'aniketvrm183@gmail.com', 'avilb', '', '', 0, '', 0, NULL, NULL),
(6, 'Uttam', 'Patil', 'Shruti', 'images/981931382655.jpg', 'images/9819313826552.jpg', 'shru@gmail.com', '', 'Gokuldham Sec-41 Turbe', 'Navi Mumbai', 410280, 'Maharashtra', 981931382655, 8080672062, 8080672062);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attendence_demo`
--
ALTER TABLE `attendence_demo`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `attendence_demoreturns`
--
ALTER TABLE `attendence_demoreturns`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `enrolement`
--
ALTER TABLE `enrolement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `felicitator`
--
ALTER TABLE `felicitator`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `felicitator_username` (`felicitator_username`),
  ADD UNIQUE KEY `felicitator_email` (`felicitator_email`),
  ADD UNIQUE KEY `felicitator_uid` (`felicitator_uid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_email` (`student_email`),
  ADD UNIQUE KEY `student_username` (`student_username`),
  ADD UNIQUE KEY `student_uid` (`student_uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `attendence_demo`
--
ALTER TABLE `attendence_demo`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `attendence_demoreturns`
--
ALTER TABLE `attendence_demoreturns`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `enrolement`
--
ALTER TABLE `enrolement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `felicitator`
--
ALTER TABLE `felicitator`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
