import unittest
from RDS import BaseService, LoginService, OAuth2Service, FileTransferMode, FileTransferArchive


class TestService(unittest.TestCase):
    def setUp(self):
        self.service1 = BaseService(
            "MusterService", ["fileStorage"], FileTransferMode.active, FileTransferArchive.none)
        self.service2 = BaseService(
            "BetonService", ["fileStorage"], FileTransferMode.active, FileTransferArchive.none)
        self.service3 = BaseService(
            "FahrService", ["fileStorage"], FileTransferMode.active, FileTransferArchive.none)

        self.oauthservice1 = OAuth2Service.from_service(
            self.service1,
            "http://localhost:5000/oauth/authorize",
            "http://localhost:5000/oauth/refresh",
            "ABC",
            "XYZ",
        )
        self.oauthservice2 = OAuth2Service.from_service(
            self.service2,
            "http://localhost:5001/oauth/authorize",
            "http://localhost:5001/oauth/refresh",
            "DEF",
            "UVW",
        )
        self.oauthservice3 = OAuth2Service.from_service(
            self.service3,
            "http://localhost:5001/api/authorize",
            "http://localhost:5001/api/refresh",
            "GHI",
            "MNO",
        )

    def test_compare_service(self):
        s1 = BaseService("MusterService", ["fileStorage"],
                         FileTransferMode.active, FileTransferArchive.none)
        s2 = BaseService("MusterService", ["metadata"],
                         FileTransferMode.passive, FileTransferArchive.zip)
        s3 = BaseService("FahrService", ["fileStorage"],
                         FileTransferMode.active, FileTransferArchive.none)

        os1 = OAuth2Service.from_service(
            s1,
            "http://localhost:5000/oauth/authorize",
            "http://localhost:5000/oauth/refresh",
            "ABC",
            "XYZ",
        )
        os2 = OAuth2Service.from_service(
            s2,
            "http://localhost:5000/oauth/authorize",
            "http://localhost:5000/oauth/refresh",
            "ABC",
            "XYZ",
        )
        os3 = OAuth2Service.from_service(
            s3,
            "http://localhost123:5000/oauth/authorize",
            "http://localhost123:5000/oauth/refresh",
            "WER",
            "DA",
        )
        os4 = OAuth2Service.from_service(
            s1,
            "http://localhost:5000/oauth/authorize",
            "http://localhost:5000/oauth/refresh",
            "QWE",
            "RTZ",
        )

        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)
        self.assertFalse(s1 is s2)

        self.assertEqual(os1, os2)
        self.assertEqual(os1, os4)
        self.assertNotEqual(os1, os3)

        self.assertEqual(s1, os1)

    def test_implements(self):
        with self.assertRaises(ValueError):
            LoginService("", [], FileTransferMode.active,
                         FileTransferArchive.none)

        with self.assertRaises(ValueError):
            LoginService("", ["not_working"],
                         FileTransferMode.active, FileTransferArchive.none)
        with self.assertRaises(ValueError):
            LoginService("", ["metadata", "not_working"],
                         FileTransferMode.active, FileTransferArchive.none)
        with self.assertRaises(ValueError):
            LoginService("", ["metadata", "fileStorage", "not_working"],
                         FileTransferMode.active, FileTransferArchive.none)

        LoginService("TestService", ["fileStorage"],
                     FileTransferMode.active, FileTransferArchive.none)
        LoginService("TestService", ["fileStorage", "metadata"],
                     FileTransferMode.active, FileTransferArchive.none)

    def test_service(self):
        with self.assertRaises(ValueError):
            LoginService("", [], FileTransferMode.active,
                         FileTransferArchive.none, "", "")

        with self.assertRaises(ValueError):
            LoginService("Service", [], 3, "", False, False)

        with self.assertRaises(ValueError):
            LoginService("Service", [
                         "not_working"], FileTransferMode.active, FileTransferArchive.none, False, False)

        with self.assertRaises(ValueError):
            LoginService("Service")

        LoginService("Service", ["fileStorage"])
        LoginService("Service", ["fileStorage"], FileTransferMode.active)
        LoginService("Service", ["fileStorage"], FileTransferMode.active,
                     FileTransferArchive.none)
        LoginService("Service", ["fileStorage"], FileTransferMode.active,
                     FileTransferArchive.none, False)
        LoginService("Service", ["fileStorage"], FileTransferMode.active,
                     FileTransferArchive.none, True, False)
        LoginService("Service", ["fileStorage"], FileTransferMode.active,
                     FileTransferArchive.none, False, False)

        with self.assertRaises(ValueError):
            OAuth2Service("", ["fileStorage"], FileTransferMode.active,
                          FileTransferArchive.none, "", "", "", "")
            with self.assertRaises(ValueError):
                OAuth2Service("MusterService", ["fileStorage"], FileTransferMode.active,
                              FileTransferArchive.none, "", "", "", "")
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "", ["fileStorage"], FileTransferMode.active, FileTransferArchive.none, "http://localhost:5001/oauth/authorize", "", "", "")
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "", ["fileStorage"], FileTransferMode.active, FileTransferArchive.none, "", "http://localhost:5001/oauth/refresh", "", "")
            with self.assertRaises(ValueError):
                OAuth2Service("", ["fileStorage"], FileTransferMode.active,
                              FileTransferArchive.none, "", "", "ABC", "")
            with self.assertRaises(ValueError):
                OAuth2Service("", ["fileStorage"], FileTransferMode.active,
                              FileTransferArchive.none, "", "", "", "XYZ")
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "MusterService", [
                        "fileStorage"], FileTransferMode.active, FileTransferArchive.none, "http://localhost:5001/oauth/authorize", "", "", ""
                )
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "MusterService", [
                        "fileStorage"], FileTransferMode.active, FileTransferArchive.none, "", "http://localhost:5001/oauth/refresh", "", ""
                )
            with self.assertRaises(ValueError):
                OAuth2Service("MusterService", ["fileStorage"], FileTransferMode.active,
                              FileTransferArchive.none, "", "", "ABC", "")
            with self.assertRaises(ValueError):
                OAuth2Service("MusterService", ["fileStorage"], FileTransferMode.active,
                              FileTransferArchive.none, "", "", "", "XYZ")
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "MusterService", [
                        "fileStorage"], FileTransferMode.active, FileTransferArchive.none, "http://localhost:5001/oauth/refresh", "", "", ""
                )
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "MusterService", [
                        "fileStorage"], FileTransferMode.active, FileTransferArchive.none,
                    "http://localhost:5001/oauth/authorize",
                    "http://localhost:5001/oauth/refresh",
                    "",
                    "",
                )

            # same input for authorize and refresh
            with self.assertRaises(ValueError):
                OAuth2Service(
                    "MusterService",
                    ["fileStorage"],
                    FileTransferMode.active,
                    FileTransferArchive.none,              "",
                    "http://localhost:5001/oauth/authorize",
                    "http://localhost:5001/oauth/refresh",
                    "",
                    "",
                )

    def test_service_no_protocoll(self):
        # no protocoll
        with self.assertRaises(ValueError):
            OAuth2Service(
                "MusterService",
                ["fileStorage"],
                FileTransferMode.active,
                FileTransferArchive.none,
                "localhost",
                "http://localhost:5001/oauth/refresh",
                "ABC",
                "XYZ",
            )
            OAuth2Service(
                "MusterService",
                ["fileStorage"],
                FileTransferMode.active,
                FileTransferArchive.none,
                "localhost:5001",
                "http://localhost:5001/oauth/authorize",
                "ABC",
                "XYZ",
            )
            OAuth2Service(
                "MusterService",
                ["fileStorage"],
                FileTransferMode.active,
                FileTransferArchive.none,
                "localhost:5001/oauth/authorize",
                "http://localhost:5001/oauth/refresh",
                "ABC",
                "XYZ",
            )
            OAuth2Service(
                "MusterService",
                ["fileStorage"],
                FileTransferMode.active,
                FileTransferArchive.none,
                "http://localhost:5001",
                "localhost:5001/oauth/refresh",
                "ABC",
                "XYZ",
            )
            OAuth2Service(
                "MusterService",
                ["fileStorage"],
                FileTransferMode.active,
                FileTransferArchive.none,
                "http://localhost:5001",
                "localhost:5001/oauth/authorize",
                "ABC",
                "XYZ",
            )

    def test_service_equal(self):
        # check if they are equal
        svc1 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )
        svc2 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )
        self.assertEqual(
            svc1, svc2, msg=f"Service1: {svc1}\n Service2: {svc2}")

        svc2 = OAuth2Service(
            "musterservice",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )
        self.assertEqual(
            svc1, svc2, msg=f"Service1: {svc1}\n Service2: {svc2}")

        svc2 = OAuth2Service(
            "musterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )
        self.assertEqual(
            svc1, svc2, msg=f"Service1: {svc1}\n Service2: {svc2}")

    def test_service_trailing_slash(self):
        # check if root dir is valid
        svc1 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )
        self.assertIsInstance(svc1, OAuth2Service)

        svc2 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001/",
            "http://localhost:5001/oauth/refresh/",
            "ABC",
            "XYZ",
        )
        self.assertIsInstance(svc2, OAuth2Service)

        # check if they are equal
        self.assertEqual(
            svc1, svc2, msg=f"Service1: {svc1}\n Service2: {svc2}")

    def test_service_check_raises(self):
        svc1 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
        )

        from RDS import User, Token, OAuth2Token

        with self.assertRaises(ValueError):
            svc1.refresh(Token(User("Max Mustermann"), svc1, "ABC"))
            svc1.refresh("asd")
            svc1.refresh(123)

    def test_service_give_description(self):
        text = "This is a test description."

        svc1 = BaseService(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            text
        )

        self.assertEqual(svc1.description, text)
        self.assertNotEqual(svc1.description, "This is not valid.")
        self.assertEqual(svc1.to_dict().get("description"), text)
        self.assertEqual(BaseService.from_dict(
            svc1.to_dict()).description, text)
        self.assertEqual(BaseService.from_json(
            svc1.to_json()).description, text)

        svc1 = OAuth2Service(
            "MusterService",
            ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            "http://localhost:5001",
            "http://localhost:5001/oauth/refresh",
            "ABC",
            "XYZ",
            text
        )

        self.assertEqual(svc1.description, text)

        svc1 = LoginService(
            "Service", ["fileStorage"],
            FileTransferMode.active,
            FileTransferArchive.none,
            False, False,
            text
        )

        self.assertEqual(svc1.description, text)
