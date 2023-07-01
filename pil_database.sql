-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : sam. 01 juil. 2023 à 00:27
-- Version du serveur : 8.0.30
-- Version de PHP : 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pil_database`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_level`
--

CREATE TABLE `auth_level` (
  `id` bigint NOT NULL,
  `label` varchar(255) NOT NULL,
  `description` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_level`
--

INSERT INTO `auth_level` (`id`, `label`, `description`) VALUES
(1, 'Licence 1', ''),
(2, 'Licence 2', ''),
(3, 'Licence 3', '');

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add role', 6, 'add_role'),
(22, 'Can change role', 6, 'change_role'),
(23, 'Can delete role', 6, 'delete_role'),
(24, 'Can view role', 6, 'view_role'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add level', 8, 'add_level'),
(30, 'Can change level', 8, 'change_level'),
(31, 'Can delete level', 8, 'delete_level'),
(32, 'Can view level', 8, 'view_level'),
(33, 'Can add classroom', 9, 'add_classroom'),
(34, 'Can change classroom', 9, 'change_classroom'),
(35, 'Can delete classroom', 9, 'delete_classroom'),
(36, 'Can view classroom', 9, 'view_classroom'),
(37, 'Can add subject', 10, 'add_subject'),
(38, 'Can change subject', 10, 'change_subject'),
(39, 'Can delete subject', 10, 'delete_subject'),
(40, 'Can view subject', 10, 'view_subject'),
(41, 'Can add time table', 11, 'add_timetable'),
(42, 'Can change time table', 11, 'change_timetable'),
(43, 'Can delete time table', 11, 'delete_timetable'),
(44, 'Can view time table', 11, 'view_timetable');

-- --------------------------------------------------------

--
-- Structure de la table `auth_role`
--

CREATE TABLE `auth_role` (
  `id` bigint NOT NULL,
  `label` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_role`
--

INSERT INTO `auth_role` (`id`, `label`) VALUES
(1, 'Administrateur'),
(2, 'Professeur'),
(3, 'Étudiant');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` bigint NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `create_at` datetime(6) NOT NULL,
  `role_id` bigint NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `level_id` bigint DEFAULT NULL,
  `image_path` varchar(50) NOT NULL,
  `otp` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `last_login`, `username`, `lastname`, `firstname`, `email`, `password`, `phone`, `create_at`, `role_id`, `is_active`, `is_staff`, `is_superuser`, `level_id`, `image_path`, `otp`) VALUES
(2, '2023-07-01 00:26:25.163005', NULL, 'Demo', 'Admin', 'admin@test.com', 'pbkdf2_sha256$600000$0OKVf7W4m2dA6q3pK3sJIy$ZjgnORvxqHTy1EExVaNszgxJhjeuXz0b1IhgPPaoZis=', NULL, '2023-07-01 00:21:24.591571', 1, 1, 0, 0, NULL, 'default.svg', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(8, 'Auth', 'level'),
(2, 'auth', 'permission'),
(6, 'Auth', 'role'),
(7, 'Auth', 'user'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(9, 'TimeTable', 'classroom'),
(10, 'TimeTable', 'subject'),
(11, 'TimeTable', 'timetable');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-01 00:13:12.017079'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-07-01 00:13:12.224406'),
(3, 'auth', '0001_initial', '2023-07-01 00:13:12.840182'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-07-01 00:13:13.021785'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-07-01 00:13:13.039398'),
(6, 'auth', '0004_alter_user_username_opts', '2023-07-01 00:13:13.070714'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-07-01 00:13:13.158989'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-07-01 00:13:13.172321'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-07-01 00:13:13.199726'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-07-01 00:13:13.219484'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-07-01 00:13:13.238083'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-07-01 00:13:13.292443'),
(13, 'auth', '0011_update_proxy_permissions', '2023-07-01 00:13:13.312712'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-07-01 00:13:13.331816'),
(15, 'Auth', '0001_initial', '2023-07-01 00:13:13.621636'),
(16, 'Auth', '0002_alter_user_role', '2023-07-01 00:13:13.871332'),
(17, 'Auth', '0003_user_is_active_user_is_staff', '2023-07-01 00:13:14.035775'),
(18, 'Auth', '0004_user_groups_user_is_superuser_user_user_permissions', '2023-07-01 00:13:14.903243'),
(19, 'Auth', '0005_level_user_level', '2023-07-01 00:13:15.219299'),
(20, 'Auth', '0006_level_description', '2023-07-01 00:13:15.318347'),
(21, 'Auth', '0007_user_image_path', '2023-07-01 00:13:15.453356'),
(22, 'Auth', '0008_alter_user_image_path', '2023-07-01 00:13:15.475103'),
(23, 'Auth', '0009_alter_user_image_path', '2023-07-01 00:13:15.847478'),
(24, 'Auth', '0010_user_otp', '2023-07-01 00:13:15.993125'),
(25, 'TimeTable', '0001_initial', '2023-07-01 00:13:16.892239'),
(26, 'TimeTable', '0002_alter_user_options_alter_user_managers_and_more', '2023-07-01 00:13:18.106811'),
(27, 'TimeTable', '0003_remove_user_groups_remove_user_role_and_more', '2023-07-01 00:13:18.598652'),
(28, 'TimeTable', '0004_alter_subject_level_alter_timetable_level_and_more', '2023-07-01 00:13:18.963442'),
(29, 'TimeTable', '0005_classroom_description_classroom_status', '2023-07-01 00:13:19.081780'),
(30, 'TimeTable', '0006_rename_start_end_timetable_end_time_and_more', '2023-07-01 00:13:19.191333'),
(31, 'TimeTable', '0007_timetable_week', '2023-07-01 00:13:19.270832'),
(32, 'TimeTable', '0008_alter_timetable_week', '2023-07-01 00:13:19.382435'),
(33, 'admin', '0001_initial', '2023-07-01 00:13:19.660803'),
(34, 'admin', '0002_logentry_remove_auto_add', '2023-07-01 00:13:19.731474'),
(35, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-01 00:13:19.806387'),
(36, 'sessions', '0001_initial', '2023-07-01 00:13:19.896493');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('dsccdtfphofzmhr5dsh2v6ktxx7gwb8c', '.eJxVjDsOwjAQBe_iGlnxhvhDSZ8zWJvdNQ4gW4qTCnF3iJQC2jcz76UibmuOW5MlzqwuCtTpd5uQHlJ2wHcst6qplnWZJ70r-qBNj5XleT3cv4OMLX_rwVsgIrSG2KIRQevSxBK6QJDApTOzgJe-Yy8U0A3SmzR4b70DAKveHxJuOHo:1qFORV:E_o6QJkNmEcMZSzzUr5cJYGuak2ntU-52B-0GCaavMY', '2023-07-15 00:26:25.171577');

-- --------------------------------------------------------

--
-- Structure de la table `timetable_classroom`
--

CREATE TABLE `timetable_classroom` (
  `id` bigint NOT NULL,
  `label` varchar(255) NOT NULL,
  `capacity` int DEFAULT NULL,
  `description` longtext,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `timetable_subject`
--

CREATE TABLE `timetable_subject` (
  `id` bigint NOT NULL,
  `label` varchar(255) NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `total_time` int NOT NULL,
  `level_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `timetable_timetable`
--

CREATE TABLE `timetable_timetable` (
  `id` bigint NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `classroom_id` bigint NOT NULL,
  `level_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `week` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_level`
--
ALTER TABLE `auth_level`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `label` (`label`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `auth_role`
--
ALTER TABLE `auth_role`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `Auth_user_role_id_5dfbbc57_fk_Auth_role_id` (`role_id`),
  ADD KEY `Auth_user_level_id_1d99760f_fk_Auth_level_id` (`level_id`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Auth_user_groups_user_id_group_id_921b23aa_uniq` (`user_id`,`group_id`),
  ADD KEY `Auth_user_groups_group_id_7f08c832_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Auth_user_user_permissions_user_id_permission_id_26a4eb17_uniq` (`user_id`,`permission_id`),
  ADD KEY `Auth_user_user_permi_permission_id_1375db89_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_Auth_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `timetable_classroom`
--
ALTER TABLE `timetable_classroom`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `timetable_subject`
--
ALTER TABLE `timetable_subject`
  ADD PRIMARY KEY (`id`),
  ADD KEY `TimeTable_subject_level_id_291b644b_fk_Auth_level_id` (`level_id`);

--
-- Index pour la table `timetable_timetable`
--
ALTER TABLE `timetable_timetable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `TimeTable_timetable_classroom_id_3b82381e_fk_TimeTable` (`classroom_id`),
  ADD KEY `TimeTable_timetable_subject_id_c330b31c_fk_TimeTable_subject_id` (`subject_id`),
  ADD KEY `TimeTable_timetable_user_id_b99d50b0_fk_Auth_user_id` (`user_id`),
  ADD KEY `TimeTable_timetable_level_id_39c24345_fk_Auth_level_id` (`level_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_level`
--
ALTER TABLE `auth_level`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT pour la table `auth_role`
--
ALTER TABLE `auth_role`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT pour la table `timetable_classroom`
--
ALTER TABLE `timetable_classroom`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `timetable_subject`
--
ALTER TABLE `timetable_subject`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `timetable_timetable`
--
ALTER TABLE `timetable_timetable`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD CONSTRAINT `Auth_user_level_id_1d99760f_fk_Auth_level_id` FOREIGN KEY (`level_id`) REFERENCES `auth_level` (`id`),
  ADD CONSTRAINT `Auth_user_role_id_5dfbbc57_fk_Auth_role_id` FOREIGN KEY (`role_id`) REFERENCES `auth_role` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `Auth_user_groups_group_id_7f08c832_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `Auth_user_groups_user_id_851066aa_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `Auth_user_user_permi_permission_id_1375db89_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `Auth_user_user_permissions_user_id_36d68527_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `timetable_subject`
--
ALTER TABLE `timetable_subject`
  ADD CONSTRAINT `TimeTable_subject_level_id_291b644b_fk_Auth_level_id` FOREIGN KEY (`level_id`) REFERENCES `auth_level` (`id`);

--
-- Contraintes pour la table `timetable_timetable`
--
ALTER TABLE `timetable_timetable`
  ADD CONSTRAINT `TimeTable_timetable_classroom_id_3b82381e_fk_TimeTable` FOREIGN KEY (`classroom_id`) REFERENCES `timetable_classroom` (`id`),
  ADD CONSTRAINT `TimeTable_timetable_level_id_39c24345_fk_Auth_level_id` FOREIGN KEY (`level_id`) REFERENCES `auth_level` (`id`),
  ADD CONSTRAINT `TimeTable_timetable_subject_id_c330b31c_fk_TimeTable_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `timetable_subject` (`id`),
  ADD CONSTRAINT `TimeTable_timetable_user_id_b99d50b0_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
