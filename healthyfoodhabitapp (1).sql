-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2026 at 03:53 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthyfoodhabitapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `ai_recommendations`
--

CREATE TABLE `ai_recommendations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `recommendation` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ai_recommendations`
--

INSERT INTO `ai_recommendations` (`id`, `user_id`, `recommendation`, `created_at`) VALUES
(1, 1, 'Increase protein intake and reduce sugar.', '2026-03-01 16:26:59');

-- --------------------------------------------------------

--
-- Table structure for table `meals`
--

CREATE TABLE `meals` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `meal_type` varchar(50) NOT NULL,
  `food_text` text NOT NULL,
  `calories` float DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `carbs` float DEFAULT NULL,
  `fat` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `meals`
--

INSERT INTO `meals` (`id`, `user_id`, `meal_type`, `food_text`, `calories`, `protein`, `carbs`, `fat`, `created_at`) VALUES
(1, 1, 'breakfast', 'tea', 40, 0, 10, 0, '2026-03-07 02:58:37'),
(2, 1, 'breakfast', 'tea', 40, 0, 10, 0, '2026-03-07 02:58:37'),
(3, 1, 'lunch', 'chicken salad', 0, 0, 0, 0, '2026-03-07 02:58:37'),
(4, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 08:39:26'),
(5, 2, 'breakfast', 'boiled egg', 100, 5, 15, 3, '2026-03-07 08:39:36'),
(6, 2, 'breakfast', 'pongal and Sambar', 100, 5, 15, 3, '2026-03-07 08:40:12'),
(7, 2, 'breakfast', 'apple', 100, 5, 15, 3, '2026-03-07 08:40:26'),
(8, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 08:52:37'),
(9, 2, 'breakfast', 'apple', 100, 5, 15, 3, '2026-03-07 08:52:45'),
(10, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 09:20:00'),
(11, 2, 'breakfast', 'apple', 100, 5, 15, 3, '2026-03-07 09:20:08'),
(12, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 13:36:52'),
(13, 2, 'breakfast', 'apple', 100, 5, 15, 3, '2026-03-07 13:36:59'),
(15, 2, 'breakfast', 'apple', 433, 9, 50, 17, '2026-03-07 13:56:34'),
(16, 2, 'lunch', 'white rice \ndal\nsambar', 230, 24, 46, 14, '2026-03-07 13:56:49'),
(17, 2, 'snack', 'egg puff \nmushroom soup \nveg cutlet', 212, 29, 39, 7, '2026-03-07 13:57:26'),
(18, 2, 'dinner', 'upma and cocunt chutney', 392, 17, 29, 7, '2026-03-07 13:57:42'),
(19, 1, 'breakfast', '2 idli and sambar', 88.4, 8.5, 20.4, 5.1, '2026-03-07 17:15:52'),
(20, 2, 'breakfast', 'chicken', 239, 27, 0, 14, '2026-03-07 17:20:04'),
(21, 2, 'breakfast', 'apple', 0, 0, 0, 0, '2026-03-07 17:20:09'),
(22, 2, 'breakfast', 'apple', 0, 0, 0, 0, '2026-03-07 17:20:12'),
(23, 2, 'breakfast', 'Chicken', 239, 27, 0, 14, '2026-03-07 17:23:13'),
(24, 2, 'breakfast', 'eggs', 0, 0, 0, 0, '2026-03-07 17:23:18'),
(25, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 17:32:44'),
(26, 2, 'breakfast', 'chicken', 100, 5, 15, 3, '2026-03-07 17:32:52'),
(27, 2, 'breakfast', 'eggs', 100, 5, 15, 3, '2026-03-07 17:33:01'),
(28, 2, 'breakfast', 'apple', 100, 5, 15, 3, '2026-03-07 17:33:09'),
(29, 2, 'breakfast', 'chicken', 120, 4, 20, 2, '2026-03-07 17:42:09'),
(30, 2, 'breakfast', 'eggs', 120, 4, 20, 2, '2026-03-07 17:42:17'),
(31, 2, 'breakfast', 'tea and biscuits', 120, 4, 20, 2, '2026-03-07 17:42:37'),
(32, 2, 'breakfast', 'boiled meat and eggs', 120, 4, 20, 2, '2026-03-07 17:43:03'),
(33, 2, 'lunch', 'white rice \ndal', 120, 4, 20, 2, '2026-03-07 17:43:35'),
(34, 2, 'snack', 'egg puff', 120, 4, 20, 2, '2026-03-07 17:43:59'),
(35, 2, 'dinner', 'pongal and sambar', 120, 4, 20, 2, '2026-03-07 17:44:09'),
(36, 2, 'dinner', 'dosa and chutney', 120, 4, 20, 2, '2026-03-07 17:44:22'),
(37, 2, 'breakfast', 'chicken', 120, 4, 20, 2, '2026-03-07 17:48:48'),
(38, 2, 'breakfast', 'chicken', 120, 4, 20, 2, '2026-03-07 17:57:54'),
(39, 2, 'lunch', 'white rice and dal', 120, 4, 20, 2, '2026-03-07 17:58:08'),
(40, 2, 'snack', 'mushroom soup \npanipuri', 120, 4, 20, 2, '2026-03-07 17:58:22'),
(41, 2, 'dinner', 'dosa and pongal', 120, 4, 20, 2, '2026-03-07 17:58:35'),
(42, 2, 'breakfast', 'apple', 120, 4, 20, 2, '2026-03-07 17:59:11'),
(43, 2, 'breakfast', 'coffee', 120, 4, 20, 2, '2026-03-07 17:59:19'),
(44, 2, 'breakfast', 'orange', 120, 4, 20, 2, '2026-03-07 17:59:29'),
(45, 2, 'breakfast', 'mutton soup', 120, 4, 20, 2, '2026-03-07 17:59:45'),
(46, 1, 'breakfast', '2 eggs and milk', 258, 21, 13, 13, '2026-03-09 03:13:59'),
(47, 2, 'breakfast', 'chicken', 239, 27, 0, 14, '2026-03-09 05:13:21'),
(48, 2, 'breakfast', 'eggs', 155, 13, 1, 11, '2026-03-09 05:13:38'),
(49, 2, 'breakfast', 'chicken', 239, 27, 0, 14, '2026-03-09 05:27:06'),
(50, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 07:05:47'),
(51, 2, 'breakfast', 'apple', 53, 0.3, 14.1, 0.2, '2026-03-09 07:05:58'),
(52, 2, 'breakfast', 'eggs', 144.3, 12.6, 0.7, 9.4, '2026-03-09 07:06:10'),
(53, 2, 'breakfast', 'dosa and chutney', 290, 9, 39.9, 12.1, '2026-03-09 07:06:55'),
(54, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 07:08:53'),
(55, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 07:21:43'),
(56, 2, 'lunch', 'dal', 102.2, 6.6, 16, 1.9, '2026-03-09 07:21:57'),
(57, 2, 'breakfast', 'lemon rice', 122.2, 2.7, 23.8, 1.6, '2026-03-09 07:22:09'),
(58, 2, 'breakfast', 'soup', 24.6, 1.3, 2.9, 1, '2026-03-09 07:29:09'),
(59, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 08:27:32'),
(60, 2, 'breakfast', 'apple', 53, 0.3, 14.1, 0.2, '2026-03-09 08:27:42'),
(61, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 08:50:43'),
(62, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 09:19:58'),
(63, 2, 'lunch', 'lemon rice', 122.2, 2.7, 23.8, 1.6, '2026-03-09 09:20:17'),
(64, 2, 'snack', 'mushroom soup and panipuri', 294.2, 4.9, 28.1, 19.5, '2026-03-09 09:20:30'),
(65, 2, 'dinner', 'idly and pudhina pickle', 161.5, 4.8, 32.8, 1.4, '2026-03-09 09:20:49'),
(66, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-09 09:32:11'),
(67, 2, 'lunch', 'palak rice', 150.6, 5.7, 32.1, 0.6, '2026-03-09 09:32:23'),
(68, 2, 'snack', 'chicken 65', 222.6, 23.7, 0, 12.9, '2026-03-09 09:32:37'),
(69, 2, 'dinner', 'idly', 149.5, 4.3, 30.4, 1.1, '2026-03-09 09:32:46'),
(70, 2, 'breakfast', 'pongal', 156.4, 3.5, 26.4, 3.8, '2026-03-09 09:44:29'),
(71, 2, 'lunch', 'mushroom biryani', 170.9, 11.7, 20.3, 5.1, '2026-03-09 09:44:56'),
(72, 2, 'snack', 'bonda and tea', 1, 0, 0.3, 0, '2026-03-09 09:45:12'),
(73, 2, 'dinner', 'parotta', 326.8, 6.3, 44.7, 13.3, '2026-03-09 09:52:07'),
(74, 2, 'dinner', 'poori and bondha', 324.1, 5.2, 28.2, 22.7, '2026-03-11 03:40:47'),
(75, 2, 'snack', 'panipuri', 214.5, 3.5, 21.3, 14.1, '2026-03-11 07:28:27'),
(76, 2, 'breakfast', 'idly', 149.5, 4.3, 30.4, 1.1, '2026-03-11 07:45:43'),
(77, 2, 'lunch', 'coconut rice', 192, 3.1, 32.9, 5.2, '2026-03-11 07:45:53'),
(78, 2, 'snack', 'carrot chips', 574.8, 7.2, 62.6, 34.6, '2026-03-11 07:46:05'),
(79, 2, 'dinner', 'pulao and boiled egg', 308.4, 15.1, 26.9, 15.4, '2026-03-11 07:46:22'),
(80, 2, 'lunch', 'egg fry', 455.7, 15.9, 41.3, 24.6, '2026-03-11 07:46:54'),
(81, 2, 'dinner', 'biryani', 142.9, 9.6, 15, 4.6, '2026-03-11 10:10:31'),
(82, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-12 03:10:08'),
(83, 2, 'lunch', 'lemon rice', 122.2, 2.7, 23.8, 1.6, '2026-03-12 03:10:26'),
(84, 2, 'snack', 'chicken lollipop', 621.6, 23.7, 99, 13.1, '2026-03-12 03:10:38'),
(85, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-12 03:10:47'),
(86, 2, 'breakfast', 'idly', 149.5, 4.3, 30.4, 1.1, '2026-03-12 03:23:02'),
(87, 2, 'lunch', 'coconut rice', 192, 3.1, 32.9, 5.2, '2026-03-12 03:23:14'),
(88, 2, 'snack', 'french fries \npanipuri', 312.5, 3.4, 42.1, 14.4, '2026-03-12 03:23:25'),
(89, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-12 03:23:33'),
(90, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 03:15:15'),
(91, 2, 'lunch', 'tomato rice', 97.5, 1.8, 16, 3.1, '2026-03-13 03:15:34'),
(92, 2, 'snack', 'panipuri \ntea and biscuits', 560.6, 10.4, 66.1, 30.4, '2026-03-13 03:15:45'),
(93, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-13 03:15:53'),
(94, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 03:46:18'),
(95, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 04:38:43'),
(96, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 04:47:01'),
(97, 2, 'lunch', 'lemon rice', 122.2, 2.7, 23.8, 1.6, '2026-03-13 04:47:13'),
(98, 2, 'breakfast', 'poori', 324.1, 5.2, 28.2, 22.7, '2026-03-13 04:57:02'),
(99, 2, 'lunch', 'chicken biryani \nchicken 65 \nmutton fry', 23619.5, 270.5, 3104.7, 1134.2, '2026-03-13 05:00:29'),
(100, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 05:05:47'),
(101, 2, 'lunch', 'biryani', 142.9, 9.6, 15, 4.6, '2026-03-13 05:05:55'),
(102, 2, 'snack', 'chicken 65', 222.6, 23.7, 0, 12.9, '2026-03-13 05:06:09'),
(103, 2, 'dinner', 'dosa \nidly', 170.5, 4, 30, 3.8, '2026-03-13 05:06:31'),
(104, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-13 05:26:48'),
(105, 2, 'lunch', 'egg rice', 274.4, 15.2, 29.1, 10, '2026-03-13 05:27:01'),
(106, 2, 'snack', 'egg bonda', 147, 12.5, 0.7, 9.7, '2026-03-13 05:27:09'),
(107, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-13 05:27:17'),
(108, 2, 'breakfast', 'rice rasam', 153.3, 3.6, 31.9, 1.6, '2026-03-13 06:29:15'),
(109, 2, 'lunch', 'aloo paratha', 231.1, 4.7, 34.6, 8, '2026-03-13 06:29:39'),
(110, 2, 'breakfast', 'panner rice', 127.4, 2.7, 28.4, 0.3, '2026-03-13 06:57:25'),
(111, 2, 'breakfast', 'butter milk and dates', 315.5, 5.7, 80.5, 1.3, '2026-03-13 07:06:14'),
(112, 2, 'breakfast', 'chicken', 222.6, 23.7, 0, 12.9, '2026-03-14 03:05:59'),
(113, 2, 'lunch', 'lemon rice', 122.2, 2.7, 23.8, 1.6, '2026-03-14 03:06:14'),
(114, 2, 'snack', 'mushroom soup', 79.7, 1.4, 6.8, 5.4, '2026-03-14 03:06:27'),
(115, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-14 03:06:37'),
(116, 2, 'snack', 'panipuri', 214.5, 3.5, 21.3, 14.1, '2026-03-14 03:52:10'),
(117, 2, 'breakfast', 'idly', 149.5, 4.3, 30.4, 1.1, '2026-03-14 05:22:10'),
(118, 2, 'lunch', 'palak rice', 150.6, 5.7, 32.1, 0.6, '2026-03-14 05:22:32'),
(119, 2, 'snack', 'panipuri', 214.5, 3.5, 21.3, 14.1, '2026-03-14 05:22:44'),
(120, 2, 'dinner', 'masala dosa\n french fries', 627.6, 14.2, 99.7, 27.1, '2026-03-14 05:23:09'),
(121, 2, 'snack', 'pizza\negg maggi', 58.4, 7, 7.9, 0.5, '2026-03-14 05:26:34'),
(122, 2, 'breakfast', 'chicken rice', 134.9, 2.6, 23.6, 3.4, '2026-03-16 03:22:50'),
(123, 2, 'lunch', 'biryani', 142.9, 9.6, 15, 4.6, '2026-03-16 03:23:12'),
(124, 2, 'snack', 'chicken 65\nmushroom soup \ntea', 247.2, 25, 2.9, 13.9, '2026-03-16 03:23:31'),
(125, 2, 'dinner', 'dosa', 170.5, 4, 30, 3.8, '2026-03-16 03:23:44'),
(126, 2, 'breakfast', 'dosa', 170.5, 4, 30, 3.8, '2026-03-18 08:28:54'),
(127, 2, 'breakfast', '3 dosa', 495.1, 11.6, 87.1, 11, '2026-03-18 08:29:12'),
(128, 2, 'lunch', 'chicken rice', 134.9, 2.6, 23.6, 3.4, '2026-03-18 08:29:33'),
(129, 2, 'snack', 'french fries', 312.5, 3.4, 42.1, 14.4, '2026-03-18 08:29:46'),
(130, 2, 'dinner', '4 idly', 230.2, 6.6, 46.8, 1.7, '2026-03-18 08:29:58'),
(131, 2, 'breakfast', 'idly', 149.5, 4.3, 30.4, 1.1, '2026-03-19 04:09:02'),
(132, 2, 'lunch', 'biryani', 142.9, 9.6, 15, 4.6, '2026-03-19 04:09:12'),
(133, 2, 'snack', 'panipuri', 214.5, 3.5, 21.3, 14.1, '2026-03-19 04:09:20'),
(134, 2, 'dinner', 'chicken fried rice', 159.9, 10.3, 13.7, 6.8, '2026-03-19 04:09:32'),
(135, 2, 'breakfast', 'dosa', 170.5, 4, 30, 3.8, '2026-03-19 08:18:31'),
(136, 2, 'breakfast', 'dosa', 170.5, 4, 30, 3.8, '2026-03-19 08:18:57'),
(137, 2, 'breakfast', 'masala dosa', 171.7, 4, 29.7, 3.8, '2026-03-19 08:19:09'),
(138, 2, 'breakfast', 'ghee roast dosa', 1371.8, 34.5, 30, 121.5, '2026-03-19 08:19:33');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `goal` varchar(50) DEFAULT NULL,
  `otp` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `age`, `height`, `weight`, `gender`, `created_at`, `goal`, `otp`) VALUES
(1, 'Updated User', 'ranji@gmail.com', '1234', 23, 172, 67, 'Male', '2026-03-01 16:25:13', NULL, NULL),
(2, 'ranjitha', 'ranjithavangaveeti@gmail.com', 'prasu@9951', NULL, NULL, NULL, NULL, '2026-03-01 17:02:18', 'Weight Loss', '164887'),
(5, 'Test User', 'testuser@gmail.com', '1234', 22, 170, 65, 'Male', '2026-03-03 02:49:29', NULL, NULL),
(6, 'Ranji Updated', 'ranji123@gmail.com', '123456', 22, 160, 55, 'Female', '2026-03-03 04:24:56', 'Weight Loss', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `wellness`
--

CREATE TABLE `wellness` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `sleep_hours` float DEFAULT NULL,
  `water_intake` float DEFAULT NULL,
  `steps` int(11) DEFAULT NULL,
  `mood` varchar(50) DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `record_date` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wellness`
--

INSERT INTO `wellness` (`id`, `user_id`, `sleep_hours`, `water_intake`, `steps`, `mood`, `weight`, `record_date`, `created_at`) VALUES
(1, 1, 7, 2.5, 8000, 'Happy', 58, '2026-03-01', '2026-03-01 16:27:45'),
(2, 1, 8, 3, 9000, 'Calm', 58, '2026-03-04', '2026-03-04 07:00:05'),
(3, 1, 8, 3, 9000, 'Calm', 58, '2026-03-04', '2026-03-04 07:18:33');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `meals`
--
ALTER TABLE `meals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `wellness`
--
ALTER TABLE `wellness`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `meals`
--
ALTER TABLE `meals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `wellness`
--
ALTER TABLE `wellness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  ADD CONSTRAINT `ai_recommendations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `wellness`
--
ALTER TABLE `wellness`
  ADD CONSTRAINT `wellness_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
