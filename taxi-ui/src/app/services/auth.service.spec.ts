import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { AuthService } from './auth.service';

beforeEach(() => {
  TestBed.configureTestingModule({
    imports: [ HttpClientTestingModule ],
    providers: [ AuthService ]
  });
  authService = TestBed.get(AuthService);
  httpMock = TestBed.get(HttpTestingController);
});

fdescribe('AuthService', () => {
  let authService: AuthService;
  beforeEach(() => {
    TestBed.configureTestingModule({
      // All module imports go here.
      imports: [ HttpClientTestingModule ],
      // All components are declared here.
      declarations: [],
      // All services are referenced here.
      providers: [ AuthService ]
    });
    authService = TestBed.get(AuthService);
  });
  it('should be created', () => {
    expect(authService).toBeTruthy();
  });
});

fdescribe('Authentication using a service', () => {
  let authService: AuthService;
  let httpMock: HttpTestingController;
});